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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ef4c83c-1083-35e0-a59f-20bb682d3d33 | -15.28636 | -43.0672 | 2026-04-12 04:04:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 33510d83-b668-322e-8f5d-c2136fb88627 | -11.80224 | -43.62589 | 2026-04-12 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 095d45c1-c580-3428-a58b-ed30cf278876 | -11.8029 | -43.62194 | 2026-04-12 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e65603f-c1fc-3d4d-aacc-beda3105894e | -11.76151 | -37.98482 | 2026-04-12 04:04:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 52240017-f00a-3667-89bf-0858dec72cc6 | -15.28301 | -43.06661 | 2026-04-12 04:04:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4e39fd42-989a-3b29-98a0-baad554921f7 | -11.80574 | -43.62648 | 2026-04-12 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce9c32db-b9e6-31f1-b641-6840dc875e49 | -11.7994 | -43.62135 | 2026-04-12 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1a0859b-c492-3259-a34d-c16a15d5b761 | -11.76509 | -37.98536 | 2026-04-12 04:04:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 06ea7b0e-9f25-3d88-94c7-cc8d5e755802 | -17.03092 | -45.84874 | 2026-04-12 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21181ba5-fe07-3f57-a6c8-64bd501958ac | -19.77205 | -49.76424 | 2026-04-12 04:06:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abb1cd21-ffc1-3636-a2b2-036d9072d233 | -19.95842 | -44.70821 | 2026-04-12 04:06:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8ed61cd6-d061-3e0c-ac03-f280a3b2ed47 | -21.44534 | -47.02244 | 2026-04-12 04:06:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2715760c-222b-33d3-85d5-1461265c8a17 | -21.44624 | -47.01911 | 2026-04-12 04:06:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ab181ce-68fd-3341-b65e-959824479949 | -22.27168 | -48.49858 | 2026-04-12 04:06:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a1e2bbd9-e9d8-390d-a238-018fea5423a2 | -21.87374 | -49.42003 | 2026-04-12 04:06:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8397b19a-4916-3995-96ea-268a5c31c1ca | -22.27068 | -48.50385 | 2026-04-12 04:06:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 56dee6df-975b-34dd-8931-f04896a7d473 | -23.407 | -46.35094 | 2026-04-12 04:06:00 | NOAA-21 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 733d4c2f-2a76-373e-94e8-2a74d67b3309 | -21.872 | -49.42069 | 2026-04-12 04:06:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 12f94885-8f53-3c87-87cb-57468e3d06cf | -23.4067 | -46.42278 | 2026-04-12 04:06:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 72d20844-5ecd-3082-8833-1e94528d8f3d | -22.27094 | -48.50195 | 2026-04-12 04:06:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 2097b8f5-f7d7-39f0-82de-0de0e0b4f8de | -23.50635 | -46.55937 | 2026-04-12 04:06:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3f7bfb3f-f3a1-3706-8333-cb2e8ed3c7d6 | -26.97595 | -50.38958 | 2026-04-12 04:08:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 349c533b-8f3a-30fc-9135-c39ed8dd6aba | 1.2853 | -60.3126 | 2026-04-12 04:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b7c590a4-79eb-3eb8-b809-de2102289095 | 1.2853 | -60.3126 | 2026-04-12 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 5b62f182-1a82-30e2-bbaf-780bd78901e6 | -9.80332 | -37.46044 | 2026-04-12 04:34:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0125b2d1-9b87-3e1d-a995-5e0c585ab504 | -9.79635 | -37.47094 | 2026-04-12 04:34:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 59bbdf28-49f4-3a9e-9900-249135d656a4 | -9.80236 | -37.46793 | 2026-04-12 04:34:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ec454286-298f-39d1-9e7f-3f08a2c47e9d | -9.80188 | -37.47171 | 2026-04-12 04:34:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ee914f66-686b-379c-831f-3a6b8f25ce8b | -11.79236 | -43.62049 | 2026-04-12 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f45a2972-48ca-31e9-9d11-5c361e6be871 | -9.80285 | -37.46412 | 2026-04-12 04:34:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0b80c70f-cc4c-35e4-a54d-1063f70a3ab4 | -11.79991 | -43.62163 | 2026-04-12 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ae0777b-c9ef-340f-919b-dfd7980f684d | -11.79546 | -43.62571 | 2026-04-12 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6ffa728-0a96-3ad3-8a0d-f74d061bd32d | -9.79683 | -37.46717 | 2026-04-12 04:34:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1977aa77-745b-39ff-9e6b-71c0c6947fbf | -11.79478 | -43.63035 | 2026-04-12 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f332ec92-b005-361b-8eb9-fa7e318b5676 | -9.80141 | -37.47537 | 2026-04-12 04:34:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2e1ed8e4-c24d-3528-960e-2d6a1af6328e | -8.78854 | -44.82224 | 2026-04-12 04:34:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44810777-c67e-34e2-ad89-07753026782a | -8.57116 | -37.0031 | 2026-04-12 04:34:00 | NPP-375D | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 99caacce-1f43-3c98-a05f-60980517d051 | -11.80369 | -43.6222 | 2026-04-12 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72268f6c-ed83-3b7d-afd2-71866abc9156 | -11.79923 | -43.62628 | 2026-04-12 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 637c4e64-8185-3e65-96b9-a42dd70371e8 | -11.79614 | -43.62106 | 2026-04-12 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8153ea4-3d17-38cd-b6e0-ec986076cec5 | -9.79588 | -37.47458 | 2026-04-12 04:34:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ee72d6d5-321e-39d3-8abd-1a3a182d5821 | -7.83031 | -42.04234 | 2026-04-12 04:34:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 85312e60-956c-300c-a7ca-a57f7ac5b55d | -9.79732 | -37.46337 | 2026-04-12 04:34:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a8f21a5e-f487-3062-a404-5f79c9b385ed | -15.28623 | -43.06831 | 2026-04-12 04:36:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 17210de8-e0bc-39d7-94e6-4c5dcfa381cc | -12.97702 | -54.68434 | 2026-04-12 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8b78f98-9c97-3905-a820-c79caff64f81 | -14.7681 | -47.15887 | 2026-04-12 04:36:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e20893a2-fc5d-3d60-835a-b905a65a3c9c | -12.60525 | -43.31943 | 2026-04-12 04:36:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8048c1b1-43c7-30cd-8e68-f3157bfc713c | -15.37711 | -52.75378 | 2026-04-12 04:36:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5db79e4e-5606-3458-b86c-9661e633e03a | -14.82593 | -53.22115 | 2026-04-12 04:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4776264c-dff6-3c5d-a4ef-6385c946a205 | -15.3809 | -52.75472 | 2026-04-12 04:36:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7b14550-1795-3901-93c5-296a24b06a30 | -11.34243 | -55.29955 | 2026-04-12 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fda19628-6898-3c32-843f-7a53e3d573b9 | -12.85322 | -39.84523 | 2026-04-12 04:36:00 | NPP-375D | MILAGRES | BAHIA | Brasil | 2921302 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af86ae75-51dc-3c5d-a96e-45edce46574c | -14.82874 | -53.22025 | 2026-04-12 04:36:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85e77e91-51bb-3f6d-889c-a38a5278917b | -12.97253 | -54.68346 | 2026-04-12 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0c9c346-77ff-3839-8ab8-8d1dc9a7525a | -17.03006 | -45.85021 | 2026-04-12 04:36:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f740c70-8b62-35d1-8534-b288030e10dc | -15.28212 | -43.06776 | 2026-04-12 04:36:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ec8fbdf8-1a75-3927-9560-07d9e166e8ea | -12.98237 | -54.68063 | 2026-04-12 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 262dd634-85bf-3da0-b543-4f21ae72e845 | -11.34144 | -55.30488 | 2026-04-12 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f044d94-7d08-3afe-8c91-819867b3a665 | -23.50696 | -46.55743 | 2026-04-12 04:38:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8e24c997-4978-371c-824c-18fdd2475dbd | -21.12511 | -47.93936 | 2026-04-12 04:38:00 | NPP-375D | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b68af973-d87f-3274-9eb9-4e0446294c62 | -21.30296 | -49.79672 | 2026-04-12 04:38:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 3a3091b6-bd10-3066-a8e6-198ff2605485 | -23.40814 | -46.34934 | 2026-04-12 04:38:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| ca26ec86-70cd-3dd2-88e1-d7bb0da8ddf8 | -22.27228 | -48.50008 | 2026-04-12 04:38:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8635e4c9-ad42-3309-a4c8-2090eba659a8 | -19.77516 | -49.76366 | 2026-04-12 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 898cc8f4-a245-354f-bc42-a6d47473ec7c | -18.78997 | -51.93383 | 2026-04-12 04:38:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d76c3b5e-307f-37dd-ba9b-8b5843d7e2b6 | -19.77125 | -49.76673 | 2026-04-12 04:38:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f2d1e44-d203-3c10-932b-b003f1dfd841 | -22.26888 | -48.4995 | 2026-04-12 04:38:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e14dd53b-c780-3d49-bceb-ad136b9dc049 | -18.78646 | -51.93314 | 2026-04-12 04:38:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0401150d-e774-3c41-8690-2b61a5568043 | -21.30687 | -49.79362 | 2026-04-12 04:38:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 64469de6-0135-34a4-912e-bf83350b5f33 | -23.40616 | -46.42294 | 2026-04-12 04:38:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 111f7484-6b02-301e-962b-5121d1d1258c | 1.2853 | -60.3126 | 2026-04-12 04:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 2bf2512c-322e-3c67-a287-3c8da85f52b0 | -27.31159 | -51.65815 | 2026-04-12 04:40:00 | NPP-375D | OURO | SANTA CATARINA | Brasil | 4211801 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0745eb51-ef91-3c85-b32a-a7c433d0960d | 1.21803 | -60.44957 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86609928-86e9-3ec7-b0dd-c257641024a4 | 1.37064 | -60.67309 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab9d5011-2549-3c96-bae0-07d59bb9f3b8 | 1.30693 | -60.65782 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1913dfc-333d-3147-8fba-6d8d1b150914 | 2.02129 | -61.09137 | 2026-04-12 04:51:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3a9a3c78-e40d-31b2-8ae1-5a515a028028 | 1.36984 | -60.65907 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e4f36fb-076f-3035-bd3b-a7386d104256 | 1.36116 | -60.68601 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfd5cebc-745f-3b95-bfe8-2ef259e145ec | 2.02251 | -61.09939 | 2026-04-12 04:51:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 26b3a1e7-30a6-3e42-b6f1-0bdeac4f6469 | 1.37454 | -60.66109 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f86f8549-a610-36e8-a94b-f6f99f099666 | 1.3572 | -60.68759 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74ba3e0e-39da-3089-8ee9-79c81a234f47 | 1.37218 | -60.67391 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d1941e4-2520-3349-905d-2358c9bfb980 | 1.28865 | -60.32221 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6298ad24-3cb1-37ac-916e-8a6a8a0fb712 | 1.21863 | -60.44889 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08392ab5-1506-3c64-8ebc-dc98543c1e4e | 1.37398 | -60.65741 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51c52165-8049-3e41-9191-86852d27d458 | 1.37159 | -60.67017 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a86623dc-b674-3079-a1a8-d439b7438435 | 2.66931 | -61.17662 | 2026-04-12 04:51:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07014d68-b2b0-3d7d-b6a0-2587e090d072 | 1.28321 | -60.32306 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a3d4d63-8f9d-32bd-b17c-2240d6e56eca | 1.34756 | -60.6625 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 722dddf6-cf93-3ef0-9638-acb5ddcfdd87 | 1.30749 | -60.66147 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ab5da11-7ac5-37b7-bb59-5df2f2e9f357 | 0.42612 | -60.51004 | 2026-04-12 04:51:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f1280da-06cb-30f4-b1bb-42bb9281c026 | 1.36279 | -60.68674 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9d609b5-f968-38dc-b98e-be4fcca28c44 | 1.37342 | -60.65372 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c3e6d46-615c-3af8-8d1f-4f109c7ffe43 | 1.38041 | -60.6538 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7adfb10a-84f3-3fee-afa0-f5ef83b88a20 | 1.38012 | -60.66029 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01b9a750-3171-3135-bb3b-54118ae74786 | 1.34814 | -60.66623 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b07a754c-bc20-36b8-8e51-a12e2b8f7485 | 1.31305 | -60.66058 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e9bea04-8d9e-3ddd-983a-10756b1fc46c | 2.3761 | -60.96094 | 2026-04-12 04:51:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 988607fb-8c07-3f95-96f7-ef43755ff02c | 1.376 | -60.66195 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7502f099-9d1b-34a8-83e2-a9b2831760c4 | 1.37008 | -60.66937 | 2026-04-12 04:51:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
