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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da1c729f-b3a1-3e83-981c-4ae0070bb550 | -13.52259 | -54.30878 | 2026-06-05 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8f0ee72-859e-3419-9e21-7fdb73368b5d | -12.44742 | -58.41168 | 2026-06-05 04:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fbbb7ed-49b0-3b98-9dea-54d53ca5a93f | -11.83378 | -49.43769 | 2026-06-05 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2398a68d-d9aa-3692-aae6-0c29cc9ac7b2 | -11.55913 | -52.80363 | 2026-06-05 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 03374e5f-27a4-36b2-90f9-ee510844644b | -11.00686 | -54.31346 | 2026-06-05 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ee3c67d-7871-37f6-af3c-02d542c4653a | -11.60207 | -55.3437 | 2026-06-05 04:25:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9eaea3b-71e9-377a-9e72-06382a463b39 | -12.31217 | -54.13151 | 2026-06-05 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18c2505b-d975-30c3-8e82-327a59156cdd | -12.80923 | -54.86193 | 2026-06-05 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8400a05-f05f-31c3-94f7-5815772171a8 | -14.15227 | -51.59223 | 2026-06-05 04:25:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 346e1b95-668d-3dd1-872d-75930a232977 | -19.94956 | -44.70506 | 2026-06-05 04:25:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6930c316-a61e-3db0-848b-05f0ee904474 | -20.90406 | -50.43551 | 2026-06-05 04:27:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 70501d4b-c44b-3f3d-985a-f0d69216803b | -21.09525 | -49.76145 | 2026-06-05 04:27:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 74dca7a3-b464-3fc2-a747-247327896376 | -19.16825 | -55.18608 | 2026-06-05 04:27:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ef0be2a5-a387-341b-8242-c44d95413f16 | -21.19912 | -48.27072 | 2026-06-05 04:27:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 015c77eb-5e80-34f8-b252-fda75da5c602 | -21.81003 | -49.11876 | 2026-06-05 04:27:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6228480d-19f7-3fc1-97a9-d85c57f6164b | -19.74185 | -53.5415 | 2026-06-05 04:27:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 98cf73dd-4c23-3088-8dbb-6e2298ea700b | -21.80588 | -49.12214 | 2026-06-05 04:27:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 854bb6d8-99a6-38b4-8c39-d3f0cda59037 | -21.80658 | -49.11808 | 2026-06-05 04:27:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5ae759cc-ada8-364f-b0b6-9646ecb5e648 | -23.14787 | -47.08503 | 2026-06-05 04:27:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f0f35f5c-2331-395f-9f1d-cb11f584ffb0 | -22.91046 | -47.24015 | 2026-06-05 04:27:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c8e1a85a-be7a-37ee-ba8c-1578b275c80d | -19.73639 | -53.54524 | 2026-06-05 04:27:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6bbe9691-8ff1-3fa4-8729-ad8560a28de6 | -22.91106 | -47.23639 | 2026-06-05 04:27:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 111b046c-fdb2-3b57-9c37-499eb3b738c9 | -19.73894 | -53.54846 | 2026-06-05 04:27:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| dd4b7416-e05d-3ac7-9620-5e5049f499f3 | -18.9241 | -53.23018 | 2026-06-05 04:27:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdf564a4-c789-3495-97e2-736ace1afe2f | -21.80728 | -49.11401 | 2026-06-05 04:27:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 719f1140-05fd-3997-a309-ac3e60a62f77 | -21.80934 | -49.12282 | 2026-06-05 04:27:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0d1e6230-59c3-3139-a0a1-164d07c0a52d | -21.27345 | -48.61711 | 2026-06-05 04:27:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1e0ed189-597f-364d-9bee-c1fe9becf7ab | -19.74342 | -53.54954 | 2026-06-05 04:27:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e2eba31b-8e95-3032-8c97-a216669f08b7 | -22.09285 | -47.06412 | 2026-06-05 04:27:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0238e03-9d16-3929-9ff3-5c2c0716efb4 | -20.90488 | -50.43098 | 2026-06-05 04:27:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c2fdac39-aebb-3263-a9d3-bbc79ec33b2c | -19.73987 | -53.5437 | 2026-06-05 04:27:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e47d27cd-722b-3995-88d6-0d104518621f | -19.16888 | -55.18298 | 2026-06-05 04:27:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| bd5d7d15-f2d6-3615-b18e-e0a8e206883f | -23.81801 | -48.7098 | 2026-06-05 04:27:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84480d7e-be0e-3805-820e-7cadff951c47 | -22.08952 | -47.06351 | 2026-06-05 04:27:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88c65ca5-00e9-3f62-8769-659d17c5b327 | -22.30653 | -47.26678 | 2026-06-05 04:27:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f74f34c5-7a25-3b17-929b-56b836c85df4 | -22.30986 | -47.26739 | 2026-06-05 04:27:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38aa3df8-f8bd-3171-9089-5c50e2cdfb4d | -19.74088 | -53.54625 | 2026-06-05 04:27:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5a387821-76c4-3c9a-8978-ec9fae2c894e | -20.28161 | -46.47871 | 2026-06-05 04:27:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60bb778b-0a94-3246-bdc8-cf84d2512fcd | -21.19977 | -48.26686 | 2026-06-05 04:27:00 | NPP-375D | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed2ada31-543e-33e3-8e3e-cb4a2a926638 | -22.30926 | -47.27114 | 2026-06-05 04:27:00 | NPP-375D | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e89b4c4-d50b-3326-b20b-4a6ec05e84b2 | -20.66199 | -45.50391 | 2026-06-05 04:27:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 786e6818-ebdb-398d-b9ff-72c5116bb9ae | -19.73991 | -53.55104 | 2026-06-05 04:27:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0894ba98-ec48-320b-824f-96c685f9c080 | -19.738 | -53.55326 | 2026-06-05 04:27:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 37d37789-29a0-3fb7-b976-42a659f6d575 | -21.27686 | -48.61778 | 2026-06-05 04:27:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 38cc775e-11b2-395e-8a1f-60c96ea4b554 | -19.73444 | -53.54745 | 2026-06-05 04:27:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 78f3f68e-df4d-3203-a64a-9d7b7ab04e7d | -19.53997 | -49.52434 | 2026-06-05 04:27:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4d74514-8fb6-3705-97a5-add9944c5d78 | -21.36028 | -46.71869 | 2026-06-05 04:27:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5edb2d53-00ee-328f-8772-8174f268e4a0 | -21.81073 | -49.1147 | 2026-06-05 04:27:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b19ece4b-4016-3dce-8865-b847b9a0b8fa | -22.67459 | -47.40586 | 2026-06-05 04:27:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 807df07f-5fef-344d-b1ef-402e0c57db5a | -3.96172 | -43.11263 | 2026-06-05 04:42:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51fca429-0851-397c-9b9e-b44ba6d80519 | -4.6323 | -43.05017 | 2026-06-05 04:42:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5213bce-4e75-3f9c-acd3-a0f10f8074cd | -5.93242 | -43.48067 | 2026-06-05 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96b18960-217c-383c-890f-e5fc00af1ee0 | -3.98829 | -47.93114 | 2026-06-05 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57bc2c1a-1150-3d46-af0a-9615e0dc6a3d | -5.81272 | -43.79323 | 2026-06-05 04:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa569003-5273-3d01-af3f-ec15cfd3eb3a | -5.72386 | -45.02786 | 2026-06-05 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 454756a7-9c72-3826-add2-0c4ef4324ae1 | -5.72243 | -45.03736 | 2026-06-05 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c855a0fd-812a-322e-b060-14655b784df3 | -5.93184 | -43.48465 | 2026-06-05 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ec255796-4385-3373-abad-a738a97d9e02 | -3.98495 | -47.93061 | 2026-06-05 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6797ccb1-3e45-3397-b62a-46bd69c181a3 | -5.30521 | -47.24154 | 2026-06-05 04:42:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99972d5a-33fc-316d-975a-736c2b974262 | -3.99162 | -47.93167 | 2026-06-05 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 225305dd-776b-3a91-a851-f19d2481731b | -5.30579 | -47.23783 | 2026-06-05 04:42:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 630c89ed-3e07-38ea-976e-d64c7b222abe | -5.72314 | -45.03262 | 2026-06-05 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6097525f-24ba-3ae4-99c5-095ea189b86b | -3.98551 | -47.9271 | 2026-06-05 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ec7aada-0f3d-3d4b-bca8-0d9fdb6451a5 | -5.30179 | -47.24099 | 2026-06-05 04:42:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97fab73e-ba25-3b0b-b0c6-839d2de2355d | -5.92815 | -43.48012 | 2026-06-05 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6c16b90-144f-3c27-be69-1175ae35ae63 | -5.933 | -43.47669 | 2026-06-05 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f90ae073-e9b3-337c-ba3c-482d19fe4a27 | -5.81329 | -43.78942 | 2026-06-05 04:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2489e61a-a9a0-3dc0-93b2-6f2ff963c6ac | -5.92873 | -43.47614 | 2026-06-05 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f500f73-89dc-33a8-9f32-ed2c409d7294 | -3.98884 | -47.92764 | 2026-06-05 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32aca7bd-9e52-32c2-9478-45112c9b126e | -3.95748 | -43.11199 | 2026-06-05 04:42:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1944528d-fe30-313c-830e-50ca8668a767 | -4.6366 | -43.0508 | 2026-06-05 04:42:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5391bfdb-7521-3b2a-994a-2607990f83e5 | -6.98388 | -42.88138 | 2026-06-05 04:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ccf3b40b-05bf-317a-8657-d8c4938d455c | -6.84686 | -47.93695 | 2026-06-05 04:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| deb6b535-8e3b-3e8c-a401-0c0badf38f6f | -7.95709 | -46.84015 | 2026-06-05 04:42:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 573b6ff4-b00b-3558-80a9-b1f10c8d84b7 | -8.37499 | -46.79781 | 2026-06-05 04:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95eab070-36b2-3a1c-a7c8-8379af6cd1d9 | -8.24419 | -47.09235 | 2026-06-05 04:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1c876e3-f8d0-35fd-8284-c88587447265 | -7.95351 | -46.83965 | 2026-06-05 04:42:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bc8c8fa-758d-3979-ad4e-66e0b5c44257 | -8.32413 | -46.99115 | 2026-06-05 04:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ec9be47-1c51-3c3b-a6d4-94a460e7c8d2 | -9.12117 | -47.95189 | 2026-06-05 04:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5263465-f88f-3106-b8ce-1a01da78e05d | -7.64132 | -45.22993 | 2026-06-05 04:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cccb42ad-d878-3f35-b87e-bc3a0fcf9d4a | -6.98839 | -42.88205 | 2026-06-05 04:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| c1121c80-9281-3cd9-86f5-7e20a772c69c | -8.40857 | -46.89148 | 2026-06-05 04:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 284b6fa4-02ac-318b-925c-7532fc9f6bdc | -8.72715 | -48.327 | 2026-06-05 04:42:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c4446698-574f-3cad-94e8-7a6afb13f32f | -7.6491 | -45.23112 | 2026-06-05 04:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2934e342-3ae7-3e90-a235-8008ca5873f9 | -8.72658 | -48.33067 | 2026-06-05 04:42:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 467a775f-ed67-3539-adf9-eb4c2b3a8226 | -6.45982 | -43.9716 | 2026-06-05 04:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c6b162b-8429-3f68-86c6-f03e0d3205cf | -8.24774 | -47.09287 | 2026-06-05 04:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf6e4345-6829-39a3-9986-74ae86d01de1 | -6.84968 | -47.94109 | 2026-06-05 04:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4db5b7d-3e0d-3529-a6e9-0e5698e85bc3 | -8.72602 | -48.33433 | 2026-06-05 04:42:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0fee4ebb-ec65-33f4-94ce-e54d6c330ed5 | -6.84629 | -47.94057 | 2026-06-05 04:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a30534df-1b5b-3a79-a112-2b7d105e1da7 | -8.37261 | -46.78918 | 2026-06-05 04:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96ded43e-5d36-3c99-a271-575f5b1c950c | -7.92022 | -46.1916 | 2026-06-05 04:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6250098-1ab4-322f-9e7d-d64dbf101e6d | -6.90718 | -48.04619 | 2026-06-05 04:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8225e8f-c5a7-3edb-8209-3fb2212ef78a | -7.91651 | -46.19114 | 2026-06-05 04:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 154415ab-e91b-38fe-8821-8b984c30b5e9 | -8.41447 | -46.90079 | 2026-06-05 04:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9e3540c-986a-36bf-9da1-44ba1c976bde | -8.48307 | -46.27549 | 2026-06-05 04:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 049c294b-92f6-3785-abec-ae3fa41f7bd1 | -8.05684 | -50.68364 | 2026-06-05 04:42:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa17ffcd-d7f0-3757-976d-8a427fc25d60 | -8.73054 | -48.32754 | 2026-06-05 04:42:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| f91a92dd-ccd5-3786-bd2b-6763a58879fc | -8.72941 | -48.33487 | 2026-06-05 04:42:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 118d02a4-1091-34ce-9412-da760452b289 | -7.64838 | -45.23602 | 2026-06-05 04:42:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README10.md)
