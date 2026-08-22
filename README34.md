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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ac561e9-ba5d-3d0a-aeec-d6b6a962d8d5 | -16.49866 | -55.18352 | 2026-08-22 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 80bc484c-3253-344e-9e26-b96d7a82a098 | -15.77973 | -48.79234 | 2026-08-22 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 258d73ce-ab10-3509-ab50-0a9cd44520d5 | -15.20264 | -52.77352 | 2026-08-22 04:29:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 03c6a146-b190-383d-8079-3960df466a30 | -16.48852 | -47.94533 | 2026-08-22 04:29:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bcbe4add-254e-3bf8-9b0e-d3e3c12e5ae0 | -18.08717 | -46.94348 | 2026-08-22 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2dac02d9-1243-3354-9a1a-6c3560870f24 | -13.82602 | -53.99125 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4d167a9-51e0-314e-9bff-8c970b080e04 | -20.08141 | -44.22802 | 2026-08-22 04:29:00 | NOAA-21 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7b60fe79-7e3d-3fc5-823c-55b749699d89 | -14.55488 | -53.05309 | 2026-08-22 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 413fea34-c521-3f35-80ae-32fe3e0dcaf4 | -17.95922 | -42.72923 | 2026-08-22 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| abbdeed6-98c9-3f75-b0a9-b82e7971fd51 | -17.33039 | -53.23089 | 2026-08-22 04:29:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0385d8f5-39ce-3886-9c80-c09af289e0f2 | -18.72534 | -42.22487 | 2026-08-22 04:29:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 799f3a2b-7dda-3538-8560-803fd974bf75 | -13.83024 | -53.99197 | 2026-08-22 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d04d9423-40a3-308d-8c0c-09ffc4ff6822 | -14.31686 | -51.86892 | 2026-08-22 04:29:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9bd2ff86-f715-3f20-8da2-0284034b7931 | -8.5406 | -54.8197 | 2026-08-22 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 6895962c-424a-3355-9822-537c222589bb | -9.1722 | -59.4629 | 2026-08-22 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| fcc903b6-e665-3f68-80d1-73dd03714aaf | -8.5404 | -54.8398 | 2026-08-22 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 63f22bd0-2aa2-39b0-9df5-729a1b9c0dfd | -6.8188 | -59.6696 | 2026-08-22 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 5dd36562-90f2-3490-b838-554d6e084e9a | -6.7507 | -58.6687 | 2026-08-22 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 6991b8e7-9c35-31cf-9216-637d395da7a4 | -8.5221 | -54.8007 | 2026-08-22 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 5ce2ea66-1277-3edd-b886-ad4b6765a989 | -6.7509 | -58.6493 | 2026-08-22 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f663f25b-ee70-310b-baec-bf14a7a0eb43 | -9.1724 | -59.4436 | 2026-08-22 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| f8d93fea-0a7f-3674-a756-9acbaa8f3e19 | -6.7693 | -58.6485 | 2026-08-22 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| c18a3319-1d7f-3add-844b-adcb6c0738c5 | -10.8172 | -50.9711 | 2026-08-22 04:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d1425c4f-0c48-3e24-a5b0-9d8e967cc97d | -6.7691 | -58.6873 | 2026-08-22 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 52314745-adcc-326e-8258-080fa65f6f16 | -6.7692 | -58.6679 | 2026-08-22 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 1684b187-583b-33d6-8a0c-1126e968ac6d | -8.522 | -54.8209 | 2026-08-22 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 1b06d84e-4327-3c36-b5db-6dda7a637a84 | -9.1536 | -59.464 | 2026-08-22 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| cb545a71-30f9-315c-8846-10d58d1021c9 | -10.7982 | -50.973 | 2026-08-22 04:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 6f9f5297-8e09-3911-96be-7ba7bfa5d8ce | -25.07121 | -49.37497 | 2026-08-22 04:32:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cd6de609-6335-33c4-8f40-8fb882354f3f | -23.82366 | -48.71547 | 2026-08-22 04:32:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b448b548-eafc-3ab5-a133-21e3eee7e906 | -24.05746 | -48.83958 | 2026-08-22 04:32:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c4ba1e88-cd83-3891-9173-c7a1fb449e76 | -23.64776 | -51.4404 | 2026-08-22 04:32:00 | NOAA-21 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1b8b04c5-3568-3120-bc50-de9892865af5 | -21.75418 | -45.45514 | 2026-08-22 04:32:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| a0699098-a653-3999-9640-6528f246a113 | -23.20838 | -47.85185 | 2026-08-22 04:32:00 | NOAA-21 | CESÁRIO LANGE | SÃO PAULO | Brasil | 3511607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d0408326-2311-39e4-bfff-d9e19b23098a | -23.52641 | -47.32468 | 2026-08-22 04:32:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f1dce1b6-fbb9-3d4b-86d7-030725d94ef6 | -21.60357 | -44.00722 | 2026-08-22 04:32:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ed29a520-50b1-3a37-b792-ec624917f22e | -21.75274 | -45.45102 | 2026-08-22 04:32:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3af5488e-2c74-3a8f-9e3a-7eb2c7c19672 | -23.20081 | -51.74064 | 2026-08-22 04:32:00 | NOAA-21 | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c426a4cb-67ea-3bed-a09c-5a4deb829298 | -23.34564 | -46.1919 | 2026-08-22 04:32:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e7be9417-4b9c-34b3-8370-a9e4168823a1 | -23.76919 | -47.44424 | 2026-08-22 04:32:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b16a72d6-6eb4-3fb8-84c1-37809e647bd1 | -20.98329 | -47.3497 | 2026-08-22 04:32:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e8c6fc0-7d53-3e28-b3fe-2cef85047f02 | -21.83084 | -44.11873 | 2026-08-22 04:32:00 | NOAA-21 | BOM JARDIM DE MINAS | MINAS GERAIS | Brasil | 3107505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 228e87f8-bb3b-3c36-9185-2438efff884b | -21.06566 | -47.34595 | 2026-08-22 04:32:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c8fee9c6-ecc0-31a1-9c86-a4d5f50544f3 | -23.22755 | -46.35688 | 2026-08-22 04:32:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1f91eb22-4380-3274-9960-a4e3a53b05cb | -21.90179 | -55.3643 | 2026-08-22 04:32:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 48ba3050-1782-3cff-a3fc-4cc7b34c6ea8 | -23.13764 | -48.66622 | 2026-08-22 04:32:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 24b13ad4-a5b7-3e36-bf4b-dd13d0f3c714 | -27.15418 | -53.40836 | 2026-08-22 04:32:00 | NOAA-21 | VICENTE DUTRA | RIO GRANDE DO SUL | Brasil | 4323101 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d668925f-7ea7-3fa2-bc0a-1b5fd9c74527 | -21.91063 | -53.38337 | 2026-08-22 04:32:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 204816e6-68a1-36bd-aa35-b0d4d4e8ce33 | -23.53115 | -47.31671 | 2026-08-22 04:32:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e110fab7-95ea-35df-8e07-2eac8209bd19 | -21.06624 | -47.34191 | 2026-08-22 04:32:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 620e4895-ef2d-31f6-96a2-4561f8261b34 | -20.6826 | -57.20218 | 2026-08-22 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1ff5da3-998c-3420-aa0f-d841450f74b1 | -21.59351 | -44.01123 | 2026-08-22 04:32:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b68531ab-a358-35df-8e7b-cd1c17a60087 | -21.06728 | -47.34479 | 2026-08-22 04:32:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 95b29db4-2bc7-3cec-b565-547e704dbb3d | -23.52997 | -47.32532 | 2026-08-22 04:32:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9274671a-475a-3f15-bdea-0b2f1cb88239 | -21.52267 | -45.11822 | 2026-08-22 04:32:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0f9910bc-0946-310b-8402-88950f364543 | -21.75209 | -45.45618 | 2026-08-22 04:32:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0e4a8daf-5b9f-33c7-bb83-a78255ffc062 | -21.49728 | -46.50661 | 2026-08-22 04:32:00 | NOAA-21 | CABO VERDE | MINAS GERAIS | Brasil | 3109501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ea3d482f-0f49-384d-8e05-da2c8345b08f | -23.25475 | -46.65697 | 2026-08-22 04:32:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d52d453b-9574-38d7-a73a-954127c57174 | -23.12187 | -49.94698 | 2026-08-22 04:32:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| cdf3e65e-02c2-377e-b219-be1ac1357f0f | -21.59769 | -44.01181 | 2026-08-22 04:32:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 4a6f2bbd-0c53-326a-8e23-dd7ba7583c77 | -22.00818 | -45.31963 | 2026-08-22 04:32:00 | NOAA-21 | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 57fe3490-df17-30ca-b738-086649313ca7 | -27.02139 | -48.869 | 2026-08-22 04:32:00 | NOAA-21 | BRUSQUE | SANTA CATARINA | Brasil | 4202909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e56c419d-7a07-3715-933a-f63c990cdaa6 | -20.98387 | -47.34558 | 2026-08-22 04:32:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf34f068-698a-37c9-85b7-e09e58794dc8 | -22.01206 | -45.32027 | 2026-08-22 04:32:00 | NOAA-21 | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 683ea7d5-55c8-3f0d-b552-7ea17c15e179 | -23.82706 | -48.71604 | 2026-08-22 04:32:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfd2ef58-8e92-3afb-a725-e8c9f7c0c4c5 | -21.60238 | -44.00831 | 2026-08-22 04:32:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 1fe116b0-f73c-3251-9846-b0a8b29c460a | -21.51908 | -45.24017 | 2026-08-22 04:32:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9d945acb-919b-35c2-9fcc-68e76cb4ad05 | -21.60188 | -44.01234 | 2026-08-22 04:32:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 3ae0c78d-15e5-3e1c-86c6-4a0fffbfab30 | -23.35007 | -46.18738 | 2026-08-22 04:32:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a4deb383-4ee9-3982-8ef9-e1693edd054c | -23.34942 | -46.19238 | 2026-08-22 04:32:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3aecd725-c817-32c1-b34f-2d71dd02a545 | -23.41986 | -47.06952 | 2026-08-22 04:32:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| eed785b7-d57b-349f-93f9-524ccab0a2fe | -21.59401 | -44.00709 | 2026-08-22 04:32:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4df14cc5-22c0-3171-84ad-822672491150 | -21.49666 | -48.04148 | 2026-08-22 04:32:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e8ade73-d2bb-3f76-b10f-83b1c879b68a | -8.522 | -54.8209 | 2026-08-22 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 5183d0eb-0c6b-33db-99b0-bf90a439896a | -6.7509 | -58.6493 | 2026-08-22 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 59f5c34a-319d-3378-a77b-8e5fcfc365a0 | -10.7982 | -50.973 | 2026-08-22 04:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 3f677c64-1b27-347a-bf26-9dde56f2b86e | -9.1722 | -59.4629 | 2026-08-22 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 05068bf6-3d43-318b-bcbe-b8e2e0c0b96e | -8.5218 | -54.8411 | 2026-08-22 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| d105ab3d-56ee-30ee-aab2-df76f99be002 | -9.1909 | -59.4619 | 2026-08-22 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 1b58c4dd-3ed1-3971-a0fd-ca481ffa1e37 | -6.7691 | -58.6873 | 2026-08-22 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 9bf5d9d2-5aca-3c1d-8f51-fb9288c4f489 | -9.1724 | -59.4436 | 2026-08-22 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 86e5c334-df85-3a08-af2e-36c30f31f177 | -6.7692 | -58.6679 | 2026-08-22 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| ed6183fb-a4b3-3da3-8fda-395edef9a561 | -8.5406 | -54.8197 | 2026-08-22 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 0d285109-45d3-350e-921b-fc8b5dfd36b4 | -8.5221 | -54.8007 | 2026-08-22 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 46c8b7a7-6095-31d8-a4b6-92146b73041f | -6.7693 | -58.6485 | 2026-08-22 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| ac32296d-d339-3a5d-8e4f-06a7dd57bb58 | -6.8188 | -59.6696 | 2026-08-22 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| edaaacfe-180d-3edb-beaa-049fb650efba | -6.7507 | -58.6687 | 2026-08-22 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 870d4eb9-8933-311d-8393-85091f0d37d0 | -10.8172 | -50.9711 | 2026-08-22 04:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 52a9b931-da7e-3469-8dbd-2bc7ac49f0e5 | -8.5404 | -54.8398 | 2026-08-22 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| c202c4e6-2358-3047-8631-c62daacb8828 | -9.1909 | -59.4619 | 2026-08-22 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 9f827411-e90b-302b-bda0-69c3f8b4ba0e | -9.1722 | -59.4629 | 2026-08-22 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 7ce4101e-ae34-3288-8c83-11e7060047e2 | -6.7693 | -58.6485 | 2026-08-22 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d4fda5bc-0a33-3ef8-bc26-98f6917ba304 | -6.7691 | -58.6873 | 2026-08-22 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| e6751417-ffa7-30dc-9154-dd9d0137be32 | -14.3937 | -51.8012 | 2026-08-22 04:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 4b3e6d5e-9b15-37a2-aff4-0563277a622c | -8.5408 | -54.7995 | 2026-08-22 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 642324fe-a0f2-3fd7-9961-e55bd66e4fce | -8.5221 | -54.8007 | 2026-08-22 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 16c5c26b-00d9-3005-a62c-1a4332b14a35 | -8.5406 | -54.8197 | 2026-08-22 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 422dd82e-ca46-3fdc-8c0b-411ce80b2890 | -6.8188 | -59.6696 | 2026-08-22 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| c78b246e-34ed-39ff-a847-dcc3ccd3ce13 | -20.6358 | -47.4322 | 2026-08-22 04:50:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 4210be35-c225-386c-9754-4d924dffd3af | -9.191 | -59.4425 | 2026-08-22 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |


[Clique aqui para ver as próximas entradas](README35.md)
