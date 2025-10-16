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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 642e23e3-65b9-3e36-9915-284845fe371d | -16.54812 | -52.43983 | 2025-10-16 05:10:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f4eaa57-0dee-3994-ac3f-4a427016afbe | -11.75701 | -61.071 | 2025-10-16 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aaa51231-df2a-3b1c-bde1-da1bc3e6e462 | -15.85618 | -53.97794 | 2025-10-16 05:10:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09fe072f-bbae-3ebf-8c3b-5095c9151801 | -11.97811 | -58.06358 | 2025-10-16 05:10:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72bd15ec-054c-3e18-a219-6d417a98294e | -15.78679 | -43.65161 | 2025-10-16 05:10:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65b79487-e837-3f4c-acaf-b80b463c1a10 | -11.0782 | -57.87929 | 2025-10-16 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d31422b4-2d0b-32e4-9d1d-94a12c29acea | -11.76079 | -61.07167 | 2025-10-16 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bebd8f47-47a7-38e7-bd79-fa96c33bd385 | -12.06249 | -51.20887 | 2025-10-16 05:10:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3c42550-e932-37ba-9491-ae63561640ba | -11.75323 | -61.07033 | 2025-10-16 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42c7ff4a-98c4-3122-872f-d34e990220c1 | -11.75915 | -61.07856 | 2025-10-16 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 324a98eb-a0e8-345d-b4ee-8e276a043dd1 | -11.8184 | -57.94563 | 2025-10-16 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0e1d0d3-cf4b-3ff1-a6f5-9af14250c3f8 | -17.93835 | -46.72837 | 2025-10-16 05:10:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b07e650-5e1b-3290-866a-ac02efb0de41 | -15.86639 | -53.96019 | 2025-10-16 05:10:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8d27da2-3c49-37b4-b19e-3db37901d827 | -12.55008 | -52.21743 | 2025-10-16 05:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 010023d2-0462-380d-b47c-09561155a3a8 | -11.76375 | -61.07458 | 2025-10-16 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1db8d640-9f91-39e6-ae0d-dd5229b44f23 | -12.60361 | -56.51274 | 2025-10-16 05:10:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dd67e1f-4299-3fda-b1ae-7b00ab46e83f | -17.93571 | -46.73098 | 2025-10-16 05:10:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67b45689-a6d2-3e51-83a5-bbf5f509c254 | -14.3697 | -56.95625 | 2025-10-16 05:10:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f607442d-1cdc-3c0c-a619-48dbe10cfd3c | -16.23354 | -59.41918 | 2025-10-16 05:10:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c4fb1e4-f4cd-3465-bb8d-54c3549754c6 | -14.22373 | -52.80737 | 2025-10-16 05:10:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e24492e8-33e5-3881-9c16-e498e81d2213 | -17.93122 | -46.73675 | 2025-10-16 05:10:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66ccc111-d3ec-3189-9a7d-1976e8be34d1 | -18.44471 | -44.48826 | 2025-10-16 05:10:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e3a3292-08a5-3628-a726-ec8852e3969d | -10.95935 | -59.12151 | 2025-10-16 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 830d05f8-26d0-3a94-8bf5-7fc497352ec9 | -12.23269 | -63.60387 | 2025-10-16 05:10:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfcb4b64-dbb1-3854-b7a0-6d2b8d557712 | -13.19549 | -49.97068 | 2025-10-16 05:10:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38e69942-32e5-35e7-87c5-4aa56a7f4d4f | -17.93169 | -46.73207 | 2025-10-16 05:10:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bdca195d-b1bc-3c5e-bf2c-148030a20e15 | -12.24184 | -49.38994 | 2025-10-16 05:10:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2bcedc8-aa6a-300a-b7bf-a122d5279342 | -17.94238 | -46.72696 | 2025-10-16 05:10:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dadfe29-60f5-3e62-b0e0-a67175dfc6ea | -11.75244 | -61.075 | 2025-10-16 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9a0bfe5-c7ba-302c-960a-4f8e34eb9052 | -13.36258 | -61.34161 | 2025-10-16 05:10:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f7f885c-2f35-34f1-a014-3d3bae2a8071 | -12.2283 | -63.60306 | 2025-10-16 05:10:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3e16274a-6df7-3863-8dbb-5e83dcc1053a | -11.72615 | -62.29526 | 2025-10-16 05:10:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cb17616-22d3-36c4-94c1-37cd0b79d202 | -13.36633 | -61.34229 | 2025-10-16 05:10:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54be6bbb-a640-3a57-8a27-2c17c8d38dd2 | -12.72171 | -48.64025 | 2025-10-16 05:10:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cfb9a10-7405-399b-a0c3-534e8a2bffd2 | -14.43597 | -52.76688 | 2025-10-16 05:10:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 561cfcd8-5907-3645-8f38-935f9cc51f26 | -16.54857 | -52.43877 | 2025-10-16 05:10:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bf5a8e6-1e92-344a-8fcf-11e02bb70513 | -11.75997 | -61.07392 | 2025-10-16 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ed41adc-cf4b-31f0-a13f-a2b847613322 | -12.17445 | -60.69259 | 2025-10-16 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 984944a2-315d-3103-ade4-3f9f5aff6d83 | -10.77293 | -62.08022 | 2025-10-16 05:10:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a568067d-c067-3db3-94cc-6e6bfb223208 | -17.93527 | -46.73572 | 2025-10-16 05:10:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 332443f1-fbe4-36b0-ace4-cbf415d69390 | -17.60826 | -46.68718 | 2025-10-16 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 111ca487-c833-344c-9584-a0db9c9b06ad | -11.87723 | -62.6899 | 2025-10-16 05:10:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48b773d7-56d5-3ee3-af74-1cbb931f4c0e | -11.75622 | -61.07566 | 2025-10-16 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cb1d028-acf5-3ee8-82f0-208c5897bbf5 | -12.23891 | -49.38834 | 2025-10-16 05:10:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 895887cc-3411-3272-b8dc-14c3cbf15cfa | -12.60751 | -56.5097 | 2025-10-16 05:10:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6af8e39a-c39b-3723-9bd2-d6e2c9987458 | -18.45181 | -44.48927 | 2025-10-16 05:10:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92f5bb25-ff44-3b15-8bde-ae98a9a34013 | -17.65159 | -48.33868 | 2025-10-16 05:10:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b8c55ce-22c7-3623-973d-f2233869322e | -12.72137 | -48.64293 | 2025-10-16 05:10:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0979195-8cfd-34be-bd72-dde8da188ff2 | -11.08108 | -57.86137 | 2025-10-16 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 56f1332e-ea4a-3baa-b4c3-b474727ca158 | -15.04128 | -52.99188 | 2025-10-16 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0476a0cf-1951-3147-8cdb-516678ed0074 | -11.76 | -61.07634 | 2025-10-16 05:10:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 24022ad6-198f-35ab-9b22-bc799f916fa8 | -17.60157 | -46.69131 | 2025-10-16 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45aaee6c-99f9-343d-b7ee-504c2da2749d | -13.65441 | -43.9404 | 2025-10-16 05:10:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b3c18b23-f7c7-3541-b1ad-1bfd10957149 | -17.60108 | -46.69613 | 2025-10-16 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 762e849b-b6ab-3a26-bc56-c5bc74d1aaee | -12.72103 | -48.64561 | 2025-10-16 05:10:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe07057f-3770-3d9c-9ad7-74bd74ee3e57 | -10.76885 | -62.0795 | 2025-10-16 05:10:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f2d1731-8b89-3dd4-98f8-b8d610a1e0c3 | -13.65511 | -43.93361 | 2025-10-16 05:10:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a4cf23e-74d6-3734-9d65-b1632086c752 | -11.38119 | -61.21052 | 2025-10-16 05:10:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe28c4d0-10ac-3a08-a697-e03f6d92b728 | -15.03729 | -52.99138 | 2025-10-16 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ff5e7b7-2e8e-3137-813b-0edf6b853340 | -15.88588 | -43.46882 | 2025-10-16 05:10:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e34e30ce-ac41-33e9-bffb-4d7ab4af8dcd | -12.05821 | -51.20822 | 2025-10-16 05:10:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60f3a967-93f6-3cec-ad8c-afe51dcb02bf | -14.79023 | -59.24831 | 2025-10-16 05:10:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 837793a1-24ef-3ad5-b09c-39b24256911d | -12.42181 | -48.69566 | 2025-10-16 05:10:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d6cabda-21e1-31b2-b31a-bfc1e956eb5e | -11.73022 | -62.29597 | 2025-10-16 05:10:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49ba9ae1-bb26-3839-bb24-4a25bbc95790 | -12.23697 | -49.38934 | 2025-10-16 05:10:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 043c439a-937d-3556-a304-8369f0e8a530 | -10.95588 | -59.1209 | 2025-10-16 05:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bd62744-1b9a-30d8-a15d-f612b6a7b40e | -15.87019 | -53.96071 | 2025-10-16 05:10:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83f42821-0c65-351d-b108-dc25fbe52442 | -12.06305 | -51.20478 | 2025-10-16 05:10:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a216cd6c-33e2-3fee-9199-4d933da793d0 | -12.55412 | -52.21801 | 2025-10-16 05:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4423583-a86d-3639-803d-2930e7f23856 | -15.86326 | -53.95489 | 2025-10-16 05:10:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c922ade6-82ba-3e89-a767-83f5df378ec0 | -15.86706 | -53.95541 | 2025-10-16 05:10:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b7ee77c-78fe-31cc-99c5-baf21984972f | -19.96747 | -49.41712 | 2025-10-16 05:12:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fe721c1e-9b49-3649-ac91-508c7caa41fe | -19.96207 | -49.41673 | 2025-10-16 05:12:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a07f69b7-8997-3144-a3c5-0474e6d20f58 | -23.69406 | -51.38779 | 2025-10-16 05:12:00 | NPP-375D | CALIFÓRNIA | PARANÁ | Brasil | 4103503 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0f594061-d626-3290-87da-6272937cf7cb | 1.05106 | -51.04083 | 2025-10-16 05:25:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9820ddf5-4df3-347f-9151-44b93efaf261 | -1.11241 | -54.06558 | 2025-10-16 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68d14c65-23a0-3352-9504-b1b648f90a66 | 1.79726 | -55.73508 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6274b3e-3da4-302a-8619-4c916a200243 | -2.25472 | -56.05775 | 2025-10-16 05:25:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b523110f-40f3-3e05-8ea9-5cbd0f2dd5af | -2.87172 | -50.74295 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3783dcae-f712-3079-9c5e-e8f3b7b1c7e9 | -3.40686 | -51.56787 | 2025-10-16 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c51629db-073a-3789-a823-86db36f11324 | 1.06393 | -51.0182 | 2025-10-16 05:25:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 14dc365e-85ff-389f-bb4e-387cfb6593ad | -1.11413 | -54.06782 | 2025-10-16 05:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3aab90de-a53b-3f0d-902b-4f9359739487 | -3.67702 | -47.63823 | 2025-10-16 05:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 624c7157-0b15-306c-91a7-ab1a9191ba93 | 1.788 | -55.75115 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f935e5b0-f78f-3d94-b7ff-be2d5a87814f | 1.23119 | -51.02852 | 2025-10-16 05:25:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 904d5620-baaa-30c6-be8c-83bfca89372a | -2.87233 | -50.73887 | 2025-10-16 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8e0fb576-f670-3a5b-b762-2419b34f60fd | 1.80404 | -55.87499 | 2025-10-16 05:25:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3eb0f51-ec3b-31c9-adcd-7392b66c9966 | -3.07711 | -49.50235 | 2025-10-16 05:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57ddad20-8190-3995-8448-c1190e7ca972 | 4.41985 | -59.7398 | 2025-10-16 05:25:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f34d70bb-9952-3cc4-b4c7-05c59ece9a58 | -1.43006 | -55.25518 | 2025-10-16 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00d65363-331a-3d90-aa3a-9fc399fb7417 | -3.05911 | -52.65488 | 2025-10-16 05:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28468073-f6ff-320f-8152-f28ccdd92dff | -3.67799 | -47.63131 | 2025-10-16 05:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44e1672c-a642-3a8f-aefd-e564d2632fd7 | -1.48826 | -55.681 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37d6d1d7-980c-3da5-b2ad-a4397e6986bc | -2.70244 | -49.86717 | 2025-10-16 05:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83ba9581-a165-347c-aaad-ecc3b5f262dc | -2.71 | -49.85864 | 2025-10-16 05:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5f45bfb-4c8f-32b3-9fd5-a9d3af7e7f1e | 1.05535 | -51.03329 | 2025-10-16 05:25:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b685bbdb-bd02-3f9b-8dcc-ce71bab2f9a7 | 1.04516 | -51.03831 | 2025-10-16 05:25:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adcda721-075b-3743-9b63-b19385b1103d | -2.70315 | -49.86251 | 2025-10-16 05:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e59a656e-c367-38d7-b64a-b6085c07e67b | -1.42588 | -55.25459 | 2025-10-16 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb55783c-935b-3827-86b0-0ec388132c82 | -2.81544 | -54.38372 | 2025-10-16 05:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README81.md)
