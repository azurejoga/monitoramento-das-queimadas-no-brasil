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

## Dados Diários - Página 292

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec7e9c3f-87da-3f67-8182-fe398ca30ed0 | -11.8975 | -47.3866 | 2026-10-09 18:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 684511a2-d835-3427-9f0c-88076d263269 | -9.9198 | -44.8585 | 2026-10-09 18:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 91ac7df6-211f-32bb-a3e1-4eab30ae61fe | -7.4886 | -42.8295 | 2026-10-09 18:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 163.9 |
| 99e5a431-2b11-3d1c-b21c-fe433e13aaf8 | -15.0713 | -41.7982 | 2026-10-09 18:30:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 119.4 |
| 0dfcafd1-7998-3393-af08-117c477d1ba7 | -14.0238 | -48.7714 | 2026-10-09 18:30:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 00785d91-881c-3375-9691-c7a84572fb21 | -7.9406 | -47.6284 | 2026-10-09 18:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 9ad1c127-2e36-305d-bf29-97e8a861a6e6 | -15.3825 | -41.9277 | 2026-10-09 18:30:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 812.6 |
| a47985c5-416f-3840-a0a1-1d1908360077 | -7.47 | -42.8078 | 2026-10-09 18:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| e910c9d5-3ed1-3e14-8256-94d54e40e625 | -10.2486 | -49.6851 | 2026-10-09 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| cfb621ff-6742-396d-b2f0-27b51711d7d0 | -3.1697 | -58.6437 | 2026-10-09 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| f4b7f2b0-15ae-37a7-ad1d-a5a5cbb3c1d9 | -3.1972 | -50.5592 | 2026-10-09 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c7ab54de-c6eb-3b55-95d4-36bbfd36061f | -11.3103 | -44.8337 | 2026-10-09 18:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| b0413ba6-526d-322b-9502-cb1092ec0a5d | -10.3548 | -46.217 | 2026-10-09 18:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 3a873937-029b-31cd-964c-07fcdd95a00a | -9.8828 | -44.794 | 2026-10-09 18:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 26d56475-90f2-3fbd-aaf6-597277fe41f3 | -13.1641 | -54.3178 | 2026-10-09 18:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| a48a1c24-3724-35e3-bb44-1e02357bf950 | -11.9677 | -43.4464 | 2026-10-09 18:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| eb1de4b8-ec51-3b4c-870c-465825326a0f | -3.4462 | -57.9812 | 2026-10-09 18:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 485b85c3-6c85-315f-b95a-272186d76701 | -6.4021 | -52.7159 | 2026-10-09 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 7438aabf-d18c-343d-a5c7-45bbb8a8e414 | -3.1786 | -50.6016 | 2026-10-09 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| c3a69ec8-b11d-3646-8400-08e2bb6b99a0 | -10.4917 | -47.2087 | 2026-10-09 18:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 236.9 |
| 14163be9-cc09-3e3e-b917-4738e5e1fdca | -4.6113 | -55.7162 | 2026-10-09 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| e89dfc3f-5059-37cd-ac16-027c6a299070 | -2.4259 | -55.9901 | 2026-10-09 18:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| dbc2ec0d-3071-3310-8189-8d3d69dc913e | -7.5162 | -45.3024 | 2026-10-09 18:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| dce3a054-bf07-3df6-a7d5-20e99e18db03 | -3.188 | -58.6241 | 2026-10-09 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 3c3725c6-bc08-317d-97a5-be1163a02a89 | -10.8909 | -44.8001 | 2026-10-09 18:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 2ec3a16a-4b73-381e-8b1a-0e72b99946d9 | -12.2119 | -44.769 | 2026-10-09 18:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 53b16c94-7246-3cdb-934d-312b7fea10f1 | -6.8098 | -52.7744 | 2026-10-09 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f0863704-74e0-3097-928f-a6d512d5b312 | -2.5492 | -58.0373 | 2026-10-09 18:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 0bbb66ee-10c7-318f-8573-afb79ab01c70 | -12.0063 | -43.4402 | 2026-10-09 18:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 195.9 |
| 75f5e00b-15fa-3550-98f3-3aa42bb1d1a2 | -2.4623 | -56.0682 | 2026-10-09 18:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6eff131a-9e7b-3b37-9cb2-0b1880dcb06d | -11.47 | -43.3824 | 2026-10-09 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| ac2bdcf2-6568-32b0-a71b-35d03428b366 | -3.0008 | -53.8874 | 2026-10-09 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 6c7d6b3f-8d21-370a-83ba-3a7a565642f4 | -9.9398 | -43.5542 | 2026-10-09 18:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 6f38a62c-4df1-394b-a97f-3861c090b442 | -10.472 | -47.2556 | 2026-10-09 18:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 33d8476a-f813-3081-bda7-d6547ae34031 | -9.75 | -44.7875 | 2026-10-09 18:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 168.2 |
| c600f58c-c83b-3baa-b80a-4f4d0434f2b0 | -9.9208 | -44.7893 | 2026-10-09 18:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 40c180d4-3606-387c-b691-20434c483209 | -2.5492 | -58.0179 | 2026-10-09 18:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 443627d6-b1bc-38bc-b358-6111a50a3926 | -12.811 | -44.627 | 2026-10-09 18:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 170.2 |
| b97312ee-0ddd-32fa-923e-2e909e09686b | -14.0472 | -43.8222 | 2026-10-09 18:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 13758776-f8c1-3ce5-9f01-1e9eb40be43b | -2.4031 | -57.9041 | 2026-10-09 18:30:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 3589b2f9-0859-3f3c-8721-3400751efb27 | -9.3162 | -47.4072 | 2026-10-09 18:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| c4dfdfa5-0649-349a-9c66-b82473066535 | -2.9795 | -54.7696 | 2026-10-09 18:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 6901dbaa-cdcb-3a10-a643-1546a6dfb3cc | -18.3327 | -42.3849 | 2026-10-09 18:30:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 149.8 |
| 15afe4db-a66d-3596-89b0-f28e03210991 | -3.1879 | -58.6433 | 2026-10-09 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 139.7 |
| 7d818977-ad51-334e-af80-03e5e100529c | -15.3832 | -41.9029 | 2026-10-09 18:30:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 499.6 |
| 021466a9-a38a-3200-b7a8-14f5c5d5f99f | -10.491 | -47.2533 | 2026-10-09 18:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 0987b057-e5a6-3085-9e85-7472d9700e96 | -2.4806 | -56.0678 | 2026-10-09 18:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 0cc5b94b-b056-3fe0-ae01-7786450e11c5 | -2.5125 | -58.0765 | 2026-10-09 18:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 792ff063-bccc-32a2-a3aa-1aa854b5d675 | -9.3156 | -47.4515 | 2026-10-09 18:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 7ef9a47a-471c-31f5-82f9-83481ade1937 | -2.8346 | -54.1326 | 2026-10-09 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b01286e7-4365-34d8-9265-28a0dfcacc5c | -13.2467 | -42.2401 | 2026-10-09 18:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 108.6 |
| d26bf96b-2a12-3ac2-8c03-5e68b15fb504 | -2.7727 | -56.5142 | 2026-10-09 18:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 9988219d-c850-3204-9bdb-5e2e612a4c26 | -14.0467 | -43.846 | 2026-10-09 18:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 87c68546-806d-32c3-aeb2-0f885a901c78 | -0.7398 | -57.9791 | 2026-10-09 18:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| f89a469e-2534-34b4-b07a-8436c052f474 | -16.9672 | -41.154 | 2026-10-09 18:30:00 | GOES-19 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 106.1 |
| df57ebb7-2235-3419-954f-3e628de79037 | -12.1627 | -45.3547 | 2026-10-09 18:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 760f76e8-a8b5-3a3a-b4fe-c4e01e378617 | -10.4897 | -47.3424 | 2026-10-09 18:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 1b7d4b64-a6f2-379d-8067-f215340fd776 | -2.7428 | -54.1347 | 2026-10-09 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 0b3b7086-dba6-39ef-aba9-d3b28d51bc03 | -2.5689 | -57.4163 | 2026-10-09 18:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| a840968d-9684-3792-b753-ab74039c025b | -3.9311 | -55.7179 | 2026-10-09 18:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 23482db1-412b-352a-b774-7ee52601848f | -14.4339 | -43.9396 | 2026-10-09 18:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 277.3 |
| 79ca4bca-ae71-361d-a197-aaff0449920c | -5.7547 | -45.3331 | 2026-10-09 18:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| b8985df4-d41f-3a52-a526-010646966047 | -3.4463 | -57.9618 | 2026-10-09 18:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| c99241eb-e626-3e5b-a97b-eb8ed4cabe51 | -2.2343 | -51.9317 | 2026-10-09 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c5be6c3c-af94-31d1-bc46-71e305923e47 | -6.4956 | -38.9535 | 2026-10-09 18:30:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 205.8 |
| 176a5ec1-bce6-389a-b417-8c1fbc1f06a5 | -2.4623 | -56.0879 | 2026-10-09 18:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 6ae38bf3-457d-30ee-9d85-91f355d5618c | -2.0577 | -56.8591 | 2026-10-09 18:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 7a357169-cbc5-383e-bc45-44e839d9c122 | -12.0448 | -43.434 | 2026-10-09 18:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 85fe6199-414c-3003-ab6b-717e9a5ee581 | -2.0576 | -56.8786 | 2026-10-09 18:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b347a556-0655-3479-be69-1e30f9865378 | -10.1763 | -48.0632 | 2026-10-09 18:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 03c6a76c-d30f-3900-b8ff-4a161c4531cf | -10.4907 | -47.2756 | 2026-10-09 18:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| eccb8d6a-6326-32d4-9bfc-c351e8b45076 | -13.3671 | -43.8742 | 2026-10-09 18:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 291.1 |
| b9a304ab-e234-330d-a84f-7004a35a5470 | -14.0667 | -43.8185 | 2026-10-09 18:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 226.0 |
| 1745b9d6-d6a9-3bde-844b-d6c3cbc3e56b | -2.4577 | -58.0194 | 2026-10-09 18:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 0f7e29b6-9596-369c-90d3-ba9f30f6c7ec | -10.3358 | -46.2193 | 2026-10-09 18:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 12690cf6-c2bc-3859-9467-c3933005fc1f | -5.561 | -43.9544 | 2026-10-09 18:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| d937bbbd-a0eb-3eec-83a3-65e1ea629dfc | -13.6896 | -49.107 | 2026-10-09 18:30:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 9c1917d1-5d92-300b-8a23-2c1dd58d22fe | -12.193 | -44.7487 | 2026-10-09 18:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 7d28f6a2-5774-3383-8435-bc82dc1cb85f | -12.5446 | -47.5875 | 2026-10-09 18:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 8b2e1433-f792-3487-ba7d-cf6d6095bb7c | -9.0362 | -44.3654 | 2026-10-09 18:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| ae32b041-138e-3a82-8c92-86c3f7aa70c8 | -18.3335 | -42.3598 | 2026-10-09 18:30:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 157.5 |
| f0134830-020a-3a2a-9c8f-421ac5548dc9 | -18.3125 | -42.3901 | 2026-10-09 18:40:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 207.6 |
| 5283ec4a-5324-3411-a0a3-64075b388921 | -3.2157 | -50.5377 | 2026-10-09 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 15fbe6ad-6c7d-3326-b205-4a8013761c04 | -3.4953 | -49.9402 | 2026-10-09 18:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 52fa9750-5760-316a-aad1-82f723a8c73b | -14.0472 | -43.8222 | 2026-10-09 18:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 606f2c3b-0cde-3a1a-b2a0-1af3f9693d08 | -7.0038 | -47.6843 | 2026-10-09 18:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| f4548a44-5a72-3bc3-9505-50a0af9cf636 | -11.8676 | -48.0348 | 2026-10-09 18:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 3a6ac17e-bfa3-393c-a98a-cd4fa360a54e | -11.8696 | -43.5568 | 2026-10-09 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 103d420f-1720-319a-acef-bf22374110f6 | -17.4581 | -45.0511 | 2026-10-09 18:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 177.2 |
| edf0932a-3001-388a-9202-bdd1e42523e1 | -2.4806 | -56.0678 | 2026-10-09 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| fcb6ec93-c864-30e3-a656-b3d64c21be1a | -9.3156 | -47.4515 | 2026-10-09 18:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 55dfcb17-8e07-3dc0-98bd-23327b14c440 | -3.5709 | -59.0969 | 2026-10-09 18:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 89749ba7-31e1-3f52-ad5d-a8b8b85b98c0 | -7.3284 | -45.2969 | 2026-10-09 18:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 443459af-71dc-3721-851e-abfefea65994 | -3.9358 | -54.5838 | 2026-10-09 18:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 1905755e-3363-389b-b48b-2af9689da180 | -15.3832 | -41.9029 | 2026-10-09 18:40:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 338.0 |
| 730f9dee-b09c-347c-947f-de9928a5e8d3 | -2.4942 | -58.0768 | 2026-10-09 18:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| c32331a7-9eda-3a18-a00a-bf8251f375fe | -16.5836 | -46.753 | 2026-10-09 18:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 6ce220af-5b8a-3aef-bd73-c56045e375d9 | -3.1114 | -53.7839 | 2026-10-09 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 13690545-14a6-3b29-aa7f-f87c5c40cca8 | -0.7398 | -57.9791 | 2026-10-09 18:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 279a86de-473b-3103-abc6-ff4e3571fb88 | -2.4395 | -58.0197 | 2026-10-09 18:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |


[Clique aqui para ver as próximas entradas](README293.md)
