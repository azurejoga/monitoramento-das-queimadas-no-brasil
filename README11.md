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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 098f98cf-f698-3340-a950-8416a38fb088 | -9.45123 | -47.85375 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c47eae9b-ac68-3015-922c-7212cd985053 | -11.18121 | -46.38745 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b081da4f-34e7-3ab9-817a-41bec180e5a0 | -4.34799 | -48.96329 | 2026-09-14 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 763b41f0-3120-381d-a297-3c558b143c6b | -10.54375 | -51.31376 | 2026-09-14 03:55:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 226ca3a5-b84d-3530-8269-674fe035e6ef | -4.27073 | -46.53408 | 2026-09-14 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daf60fb7-4cca-3589-9322-06978ecd77d2 | -3.38553 | -50.39286 | 2026-09-14 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e22e1554-37e8-306f-b332-b0d4e8fcdc70 | -10.55282 | -51.31142 | 2026-09-14 03:55:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0e2394c7-df28-3188-a85a-6cd084be139f | -11.18586 | -42.81169 | 2026-09-14 03:55:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 991cd2a9-3a39-33bb-a921-0e66b5d742f9 | -11.42838 | -45.14073 | 2026-09-14 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51fa121a-3321-3b80-adf9-19cf1bab0f60 | -7.07761 | -43.52499 | 2026-09-14 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c146a29b-186f-3cdf-841c-07cdbc11eda1 | -10.30857 | -45.27547 | 2026-09-14 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6403818e-6a41-35f0-a002-1ea65b874e08 | -7.1103 | -41.79509 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9fe31c6b-ec6b-3b88-8386-93a317fbaff0 | -6.88113 | -52.10199 | 2026-09-14 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2b9519d-6dbd-3447-aebd-dee96542868e | -9.44707 | -50.12743 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| edf7832f-33c8-3415-98ae-20ad621c1bd2 | -5.28843 | -45.26497 | 2026-09-14 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 19104ba2-27a8-3f3a-8f42-9367706b7cff | -4.55589 | -50.45895 | 2026-09-14 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c7d0c298-c19f-3bf3-adbe-8323eabb740c | -6.32332 | -44.17565 | 2026-09-14 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61e23a98-6f38-35ce-87f0-8fb41348579f | -6.20798 | -45.32252 | 2026-09-14 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 979bf637-e86e-3768-9e85-9e2e86d6f7de | -5.81509 | -42.73891 | 2026-09-14 03:55:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2aba7255-94ee-378e-8e82-06aa58083645 | -3.35197 | -51.29087 | 2026-09-14 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a74b278b-f144-3e4f-ae6a-a940d1ce6376 | -11.19446 | -42.80445 | 2026-09-14 03:55:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c3abd2ee-5416-3e78-8f15-057d86726999 | -11.18145 | -42.79361 | 2026-09-14 03:55:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0728d9b4-9858-37a4-bcb2-d2f45b82c978 | -7.11815 | -41.79216 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 12ea193d-d717-3417-8a14-bd3ef4727cc8 | -8.44359 | -46.03082 | 2026-09-14 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 54cfb202-7b16-31c3-8cb9-d602f4d79036 | -10.55092 | -51.31026 | 2026-09-14 03:55:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06bba388-fe6f-3553-a0e7-685a730b43d6 | -4.59103 | -50.98843 | 2026-09-14 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d796f198-6080-3c49-b9e8-7c781a88adcd | -6.32681 | -44.18048 | 2026-09-14 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c8f31dc-b6a6-359f-9db2-d2f8ea0b040e | -9.98897 | -50.27628 | 2026-09-14 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 647e5ed4-d29f-30de-a44d-556f9208e7c2 | -8.57827 | -44.46486 | 2026-09-14 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c30f8704-71b5-38a1-a0db-feeb92eaf7fb | -10.10245 | -48.86732 | 2026-09-14 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b1170aa2-980c-3bca-a2c4-c1962a6f319a | -7.16011 | -42.11367 | 2026-09-14 03:55:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 47582ebc-2ec9-3837-8b08-b9c82b123afa | -11.59787 | -46.77547 | 2026-09-14 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a69a838e-e9df-3ee1-a3e8-7eb4f7dd1d9d | -10.57079 | -51.34064 | 2026-09-14 03:55:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0366bec3-22c5-36b2-a890-e4fe6326e36e | -3.39405 | -50.76537 | 2026-09-14 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8743edb4-1643-35a3-8305-b61f509f9f24 | -9.46612 | -47.32528 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91c03f8a-9a15-3ac3-9936-e327f7dde47a | -9.44222 | -47.85769 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5077b27-7c1e-3506-bed0-5c07bd9c5d3b | -10.77049 | -48.97499 | 2026-09-14 03:55:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4fa3d45e-bf34-3e7d-8b71-cd9f727507c8 | -7.09458 | -41.80104 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f2d4c940-02b9-3ffa-9c64-151fa9feab4c | -11.60017 | -46.99596 | 2026-09-14 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9c707a0-7983-3f9c-ad97-6d6704daddca | -9.31593 | -44.35804 | 2026-09-14 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a55daf54-4337-3103-9ea9-8ac0ef4ac87f | -3.37945 | -50.76929 | 2026-09-14 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d363f88e-ba5a-3f32-8601-ec1de0d13b03 | -7.49902 | -38.35132 | 2026-09-14 03:55:00 | NOAA-21 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a47701ac-a6f3-3f8f-beab-e5b125dd6dd6 | -9.48825 | -45.46285 | 2026-09-14 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b95b970f-2720-3c51-bed6-17e14ebe39de | -11.37214 | -43.94999 | 2026-09-14 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34d601d4-366f-3d9d-aa4b-3ce1c62147d1 | -5.76089 | -44.05465 | 2026-09-14 03:55:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8cea1ace-b081-3e7f-bc70-2283c435dc6b | -11.18656 | -42.80747 | 2026-09-14 03:55:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bbba402d-1a4b-380a-90a8-664f57572c3d | -6.34337 | -44.10798 | 2026-09-14 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c41a1fcb-926d-31fa-a866-875ced009e9d | -11.20693 | -46.42496 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05f64ec9-53e0-3d27-a19e-ec0ba85f44a5 | -8.121 | -44.05523 | 2026-09-14 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e3902e5-5ad8-3dfb-a843-a541b729624d | -10.10988 | -48.85728 | 2026-09-14 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2a29ed26-8c3d-3d34-a6fa-41035c4e353a | -9.40165 | -50.17329 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4c72f152-af89-38dd-9dc0-2d2517d67d04 | -7.20254 | -45.92178 | 2026-09-14 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b88f54cf-3e4c-3cda-9d98-59eacec129e0 | -4.55494 | -50.4604 | 2026-09-14 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 586baf5a-ac88-3ad3-9012-97d0f052ea61 | -4.60517 | -42.59847 | 2026-09-14 03:55:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ea655074-36c1-3773-aded-26ad248d5e73 | -5.89706 | -42.68602 | 2026-09-14 03:55:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 063a9478-60fe-3224-8af3-22ed58dd6445 | -6.1745 | -43.34238 | 2026-09-14 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2163db02-8868-3683-8307-3d9b78dedddc | -7.96523 | -43.9845 | 2026-09-14 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7613641f-7ca4-3db9-a9c0-ab16bb3982f1 | -11.2265 | -46.43087 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbaa460f-4a82-3bb1-b8d8-20f924e48ae1 | -7.09817 | -41.80165 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8a68f903-d223-38fb-ad78-427cebb30f03 | -9.4518 | -47.85072 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbcdab23-96d6-324a-a668-ce93b12f9c9c | -5.11784 | -41.07758 | 2026-09-14 03:55:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a21e2c4b-4a08-30b1-bd8e-32e280d38a9b | -11.23398 | -43.44054 | 2026-09-14 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f60aed6-6dfa-301e-9e28-7a14da883873 | -9.71557 | -50.8526 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b0c57b03-1661-3dbe-b76e-53a40e5a38d6 | -7.10153 | -41.78087 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f52f3102-a5f2-38f9-95f8-1da42fff91d0 | -9.54616 | -45.43787 | 2026-09-14 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bb4f880-827c-3cf0-997c-30df23e7c285 | -6.53342 | -44.09265 | 2026-09-14 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0152b523-6439-3b5b-adad-1fcc2541b2a2 | -5.11428 | -41.07707 | 2026-09-14 03:55:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5586a6be-c344-3333-9a96-47829208f1f2 | -7.77607 | -46.66664 | 2026-09-14 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4d90e4d-ab49-3091-9526-e08f65dbac41 | -7.4232 | -41.92423 | 2026-09-14 03:55:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cd544214-5f23-3b52-9276-67a5748cab49 | -9.32783 | -44.3639 | 2026-09-14 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a03c0197-cb05-3b98-b61e-80c18acb7e23 | -9.40757 | -50.17442 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 637d80ad-1a85-3f20-81f1-d19055aced3e | -4.85332 | -48.35904 | 2026-09-14 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 216c55d6-e33f-36e7-b719-7e11d7976f2b | -10.03721 | -52.12474 | 2026-09-14 03:55:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32473624-db83-314f-9191-f2f7ed88e0e9 | -7.01907 | -44.63389 | 2026-09-14 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d760ed7-f1b9-3d75-995f-845ad1b81cf0 | -6.69426 | -43.14379 | 2026-09-14 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c780927-833e-3cbc-a97c-0560b9509e22 | -10.57801 | -51.3369 | 2026-09-14 03:55:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 530530f2-f4b2-3c6a-823c-4f5bdf06d2a8 | -11.23693 | -43.4457 | 2026-09-14 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3af206f5-7f71-37bb-8215-0b6a814a9f3f | -7.10603 | -41.79868 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a5701fe4-b1a5-3df0-85a5-b8823e36e1e8 | -6.69113 | -43.14136 | 2026-09-14 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2b569f7-a925-354e-8555-002252ad16d9 | -6.69419 | -43.14697 | 2026-09-14 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19c08c86-fa51-34b2-b033-ddf8724b35e8 | -11.37596 | -43.95065 | 2026-09-14 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 072c007d-eba8-3913-ae56-f39b4a18476b | -7.09032 | -41.80458 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1ecbf67d-96b8-3421-9a8b-4c73b3f8166d | -6.69037 | -43.14312 | 2026-09-14 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b12a6761-bdd0-3e8d-b306-436469a837cb | -6.50883 | -47.59914 | 2026-09-14 03:55:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84c1d28e-4f4f-324a-b355-a2c2e2a68d8b | -9.45359 | -47.85303 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a645d823-99be-3c85-a5ca-8494c02acd09 | -9.45301 | -40.39662 | 2026-09-14 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e1c027a3-62f6-385b-86a7-b2525aa5742a | -7.97079 | -43.9817 | 2026-09-14 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1517721c-1ab7-3945-9c57-3cbc60953d60 | -6.32266 | -44.17955 | 2026-09-14 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32e55454-af0f-381e-8bd6-c9e5491040e3 | -8.04768 | -45.54366 | 2026-09-14 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 53f41adf-59fb-34bf-91da-67739dcb5435 | -10.31561 | -45.28511 | 2026-09-14 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5052aed-2683-347a-b5ed-c221da37299f | -9.45081 | -40.38892 | 2026-09-14 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 79fc516e-75e0-3cff-8636-aa8468c232ae | -9.40426 | -50.19189 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2134d5df-171c-37a4-8808-d5ea147e1762 | -6.20775 | -45.40173 | 2026-09-14 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d97cdaf-73cb-33ae-b36e-5ff04c731752 | -6.66196 | -43.65509 | 2026-09-14 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60769ac9-a1a5-3c01-a831-ffacc8513160 | -10.64096 | -46.0948 | 2026-09-14 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7333f182-dd1b-36b4-9857-d6dd0e6b75c9 | -3.79244 | -48.92842 | 2026-09-14 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee6f92c0-a679-348b-b88e-35a0f5261b97 | -7.78672 | -46.66288 | 2026-09-14 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 226de3bd-eb26-307c-94da-3604805d3c7e | -11.18365 | -42.80264 | 2026-09-14 03:55:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8ec2bd08-bc35-3397-8238-7ad8f2788845 | -8.00083 | -43.78275 | 2026-09-14 03:55:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 55710ac4-f183-3e91-b871-adfca364583f | -9.37709 | -50.17321 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README12.md)
