# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 046d1fdb-80f1-3708-be45-32d2677c5104 | -11.32966 | -45.16101 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 472afcd7-c4f0-3b96-9f29-7298d88248f4 | -10.6239 | -48.68052 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 802577f9-811c-3ea0-a915-98c8c9d0bb1e | -8.77517 | -46.45686 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 27189502-9be8-3d52-b734-72eeb0f875d0 | -14.52535 | -52.2922 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 42b3987d-bbb7-33ea-bf9d-a47bde4f0451 | -9.41471 | -45.65151 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b4cdf5ed-6788-335f-9cb2-8b0c615f1946 | -9.60766 | -47.61879 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5fa935fb-0172-37db-8044-4093334eed88 | -14.21283 | -48.64545 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2498e96a-46fe-3a6c-aa0d-7c06cfb2eaf8 | -12.10403 | -47.2508 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7303f3ca-0112-3004-a5a8-3010a7cf2d17 | -10.07646 | -45.86469 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 65bbaf08-a8c7-3db7-ae6b-81b970f92476 | -11.32475 | -45.17999 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 7cfcdf1c-c764-3d23-9fc7-4bd8c7898d14 | -10.11526 | -45.84632 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2dbe3def-798f-344e-8a52-c8a3c9595a48 | -10.50697 | -45.03954 | 2026-08-31 16:30:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7b1043b6-482e-32e4-ac14-98a8fb72ea8e | -12.1041 | -47.27394 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 9251d840-8965-33ab-a230-fde9fcb1632b | -11.68444 | -47.59721 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d3ea5e44-b136-3599-87ed-2bd417a092af | -12.09478 | -47.14585 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1823467e-b92a-3e84-9384-69f0e5bcc6c4 | -11.6342 | -49.41577 | 2026-08-31 16:30:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 272d46c0-d0da-3d5e-92c4-84a1a7fc3404 | -11.61776 | -49.41442 | 2026-08-31 16:30:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| af719242-c2ba-3359-bf4b-54ba4e665d8a | -11.20635 | -45.10061 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 34cea7b9-5bea-3895-b973-8911c96f6d14 | -9.67257 | -47.93628 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 59a6e4d4-1a44-30b7-8ff2-03e33309ae6b | -15.40409 | -52.70452 | 2026-08-31 16:30:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 628de85a-bec9-370b-bb79-0da2b495b6c9 | -10.40146 | -45.07991 | 2026-08-31 16:30:00 | NPP-375 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 37b36d36-81df-3490-abb2-a04c1ec81b6a | -9.62024 | -38.06618 | 2026-08-31 16:30:00 | NPP-375 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c107bb0b-c19e-3824-8724-d78531fb4edf | -9.41321 | -51.68095 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4fae93a4-b48d-358a-8601-c50b478b463a | -11.37983 | -45.1673 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7a82858b-d6f8-3812-b8a1-495369557131 | -11.23536 | -51.25299 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3351c5fe-746b-351b-a3d6-f1d95f728774 | -8.76982 | -46.45539 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| a6a402d3-5adb-3895-8ef2-ab5b96bcb7c3 | -9.47129 | -48.19622 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e5d04098-a55e-3163-b3ac-b9a8dc959ccf | -11.31852 | -45.1897 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 84068928-ff16-3b06-9653-abdcc5b44e21 | -10.83115 | -46.01293 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| b7bf4946-b660-393b-896e-d5bead8c98f7 | -10.1197 | -45.85037 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4e91f3c2-482d-3f99-81f0-155c553d8d63 | -11.9345 | -45.06321 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| abc6a6f0-f6dd-316c-9d59-e881726c86e1 | -12.95781 | -45.93823 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 3bf6b4af-f454-311d-b4cc-20f7e294644e | -10.82993 | -47.23547 | 2026-08-31 16:30:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ee503fa7-db8a-3262-a134-20fb7b3c2f47 | -10.7487 | -54.03641 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 14bffdfd-0363-35f3-a8bc-157d19b9f560 | -14.58069 | -53.5878 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 13088df3-2a26-3697-824d-6b8c9365a0fa | -8.38834 | -44.98609 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 133ceec7-a89b-3ccf-9201-24a677e6b94b | -14.63711 | -53.57342 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e7558f1b-4b85-3142-80c2-934b6099fe98 | -14.57403 | -53.58867 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 8488cf9a-2c2f-3b7e-9c5b-12503b18974f | -11.91227 | -45.04803 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6469b0a3-a624-3c71-afd4-056f453a7e7a | -9.20547 | -47.99356 | 2026-08-31 16:30:00 | NPP-375 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9cfb0e5b-5bec-3f89-ba97-ef6ef6a1d1fc | -12.09376 | -44.99599 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| b73b9394-22e6-3e29-96ac-6fb137093d23 | -11.21143 | -45.32719 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 703fba37-2803-3107-a536-b3ca0532551e | -9.58798 | -47.60133 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 161ab77a-6b15-3f6d-bcae-da940e87a693 | -10.33753 | -49.9578 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| faf084c9-4a1d-3e33-86c9-637d83712846 | -14.50113 | -52.19217 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 98a83ed8-1709-389e-8fa4-3080720ff068 | -12.10195 | -45.02699 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 880ed33a-bbf8-33f5-ac1a-9c462011cbfd | -13.274 | -51.60483 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c84bf711-5e52-3db2-8164-5a158033099e | -9.66449 | -47.94157 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79133e95-b480-34ae-ac8b-f0aaac6d35b3 | -8.87642 | -46.02599 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 86bc6426-2719-35ee-82ff-326e5fd272c5 | -12.0837 | -45.74744 | 2026-08-31 16:30:00 | NPP-375 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| c721efbd-1cc9-3772-9be6-f3d1cb35d406 | -9.60184 | -47.60752 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 6b209d29-1ddf-3288-8644-66f12bab66e6 | -11.21891 | -45.32608 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05e6d690-a2de-3903-97f5-94884aaf7305 | -10.84383 | -45.31398 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 2805d229-b228-3aec-a219-1277273f74fe | -10.13685 | -45.86191 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c1cdadfd-f53f-3c20-a127-02558a766253 | -9.41661 | -45.66452 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 403bd0f0-db49-35af-8b0d-6e71d0da9c33 | -12.10058 | -47.1572 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99115575-c7bf-3414-9e2b-2fe701d33165 | -14.54035 | -51.98038 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 483208f7-7dfa-3130-ba45-850654bf7b37 | -10.02106 | -45.55967 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c06ebf90-c353-3c90-a19d-246e730ead06 | -10.51575 | -50.81813 | 2026-08-31 16:30:00 | NPP-375 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1d45410f-dd3d-33dc-a3eb-e2e30cc279c5 | -9.8173 | -46.45057 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3ee8d7c1-f0f6-3291-9cf1-628b0b37d9b7 | -11.21251 | -45.09082 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f1c52e03-2191-3816-8c15-d80330b92b7d | -10.15984 | -45.72451 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d60d56d5-2bd1-360e-8f85-b2cfc2454e4a | -12.07717 | -47.20367 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| deeb2c4f-4095-3082-93c7-3fa8738542e9 | -14.66071 | -53.5777 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d2157f9c-6fc0-3695-88f6-fc817a0d7382 | -12.09983 | -47.27453 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 3efdb148-5ed6-38ee-82bc-e24dfed7765e | -11.22961 | -45.37556 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 69d10415-cabe-32ad-9e48-034df030226f | -14.19633 | -46.56968 | 2026-08-31 16:30:00 | NPP-375 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e10d8828-f699-3f3c-a402-7f583b7b9671 | -13.66367 | -48.89809 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8b2c0be6-ae28-3a2d-b639-6971efef097b | -11.32034 | -45.20268 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7292c399-1796-35c6-b681-b3ef57b95c9f | -13.09134 | -45.17652 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e3ff2df7-dc64-3c98-811f-1048986820c0 | -11.24529 | -45.13559 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| bca0be4e-b6d5-3731-a92b-63e258456658 | -8.91934 | -45.03228 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.0 |
| d3078664-8563-3aed-aeaf-fe5380dc9f68 | -11.20771 | -50.62225 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3b0d5169-6cbe-3b9b-b8c5-32f972fb4f6a | -11.71401 | -47.61943 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 51f2d2c4-ab52-32de-943f-8aa501f83314 | -11.34583 | -45.22187 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 69bf6091-90d7-3f06-ab16-f6e14c0004d9 | -13.72451 | -41.95699 | 2026-08-31 16:30:00 | NPP-375 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6fa63731-d5ff-3e76-a587-1db0e3018fb9 | -9.59233 | -47.60083 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0ef7bd40-bae2-3285-b011-191cf0d9b520 | -11.19889 | -46.10404 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| a18947b5-4d2f-3641-93c0-025efb6d3439 | -10.16561 | -45.7378 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fb1e2424-6743-3fe1-8a17-9ab63f508831 | -11.24394 | -45.0997 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e5d3d301-f07d-3265-88df-7dd74ae61120 | -11.51873 | -46.94189 | 2026-08-31 16:30:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6bcb81b5-2717-3657-971b-2d8d968d3160 | -9.59655 | -47.60024 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4364d02d-921a-33c1-b0d9-5acb16bf2c65 | -11.03014 | -49.69945 | 2026-08-31 16:30:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f590fae3-5570-3269-8f9a-3726f190353e | -13.06692 | -40.72239 | 2026-08-31 16:30:00 | NPP-375 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5b129bf3-4113-3913-a5d7-bddc948c3331 | -10.99083 | -48.39306 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5540d976-6b20-3bb4-b782-38d0dd14ce92 | -11.51714 | -46.93044 | 2026-08-31 16:30:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9260dc8b-2b85-39b7-9fc5-6f0402afae46 | -14.57463 | -53.59431 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 86f6f824-b782-3fa7-b2d4-5d0565d6f845 | -11.23233 | -45.15084 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 64e16dc0-a10b-345f-a3da-c9aad3e006df | -12.09623 | -47.1904 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c347b884-a2aa-33cc-ac12-bd97010d606f | -14.09302 | -52.19426 | 2026-08-31 16:30:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1491978-09e4-3925-808a-60d407cd0835 | -10.14959 | -45.76058 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7194a809-5889-3c4b-a6d2-b5e70c71f5c2 | -10.10684 | -50.29127 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 207c0015-e533-3a41-a2ec-58872e9464de | -8.884 | -46.02497 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 16c12c2c-e940-336c-be2b-c287c24773db | -9.29049 | -45.39183 | 2026-08-31 16:30:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 47a5ef0c-5a72-357e-b03f-ecef18119538 | -12.11387 | -45.03062 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 136b8023-4a16-3817-b383-522980766f42 | -12.9571 | -45.93304 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| bab5035b-a293-3151-b508-777c8ea81e40 | -12.11645 | -45.0487 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86e7ac26-634d-35ea-a7d5-02ba33510d45 | -13.39737 | -51.66338 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 97cc5dfe-099c-3306-9179-296994e93bc7 | -10.7543 | -54.06629 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ff42b9d8-8e2b-3827-a3fb-6387efdd817f | -11.6719 | -47.60272 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |


[Clique aqui para ver as próximas entradas](README120.md)
