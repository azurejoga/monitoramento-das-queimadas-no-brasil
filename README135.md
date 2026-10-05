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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff3b98c5-47fd-308d-a924-3c6e519c4f69 | -3.49094 | -59.58033 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f99c53a-1f24-38cf-8a78-e8fb41d6e47a | -3.37027 | -58.18747 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3e25b243-73d0-3e6a-9e2b-cdc183691c03 | -3.66925 | -54.5332 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4d92fa5d-b281-3882-9962-1a7a7bf2f930 | -13.50528 | -61.1314 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0065b88b-472a-3500-98fc-c50db0491a20 | -7.97168 | -69.89571 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0557772e-e9c7-3b6b-b6b9-e49828887d13 | -3.65661 | -59.15961 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fa1c41f3-ed06-3608-a683-143757de66c6 | -3.08249 | -54.17237 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| bb483fee-15cb-3cfa-945e-de31397d56c7 | -3.38954 | -59.4276 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d16edd63-fa93-38da-9604-b5a97cd40930 | -11.43895 | -47.6847 | 2026-10-05 17:34:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6aac99f-7ec9-3c77-9e39-b06b91cdf398 | -4.69024 | -54.4888 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 9b434d67-9801-3ae7-a4ee-fe2664f8d5e3 | -3.06809 | -54.1699 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| efce3b32-7929-3ffc-9a59-89892a8603bc | -6.17293 | -55.38009 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87a02d3a-b31c-30da-a62a-727355d00332 | -3.69446 | -55.95883 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| d8d92db9-8a28-3bf1-abd3-7abb662675b5 | -3.8855 | -55.79938 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 8ef56fe1-3fc2-3c11-a01f-dc383037cb4b | -6.83007 | -58.58762 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a480b2cb-3d84-3bd4-a15a-534d1f1236a7 | -7.58843 | -46.07756 | 2026-10-05 17:34:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0e8db207-c97b-369d-9de5-d36271a234a4 | -3.46723 | -54.59411 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7e7529df-d067-3c01-a4fc-9aeef631ef68 | -3.28589 | -59.41449 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 72aa7f91-a0fb-31c8-b62f-68fb24a0b6e8 | -3.08171 | -54.16764 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 9edef761-a66c-3e34-b9f5-549d3c32e699 | -8.02482 | -70.07569 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 43ac2327-82ee-3d4b-ae0d-37943485d447 | -3.28003 | -54.17946 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 921a263f-3648-3a2e-ae98-9698a3a2fb0c | -6.17786 | -55.71104 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e444ae9f-7760-3352-be33-19b810f51d9a | -8.34879 | -70.10137 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 6476ae7d-bc46-39a5-a26a-0ba4be31dd64 | -5.81938 | -53.83676 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 0a80f527-85f0-31bc-8bca-928f335d65cc | -8.08356 | -71.22082 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2748be82-6a1f-3c35-9819-965decd5f75d | -2.94573 | -54.14315 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 5faa9032-fcc9-319e-88c7-ac98f33d8eba | -4.0536 | -54.04501 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 78a34116-e2f7-3875-94af-6741d9b0aaca | -2.92747 | -54.14605 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 48256bf9-0fcb-3035-8c02-4de9076e39bc | -4.44826 | -54.97296 | 2026-10-05 17:34:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 30aab526-600b-35ac-be4d-c6fe9a0de9ec | -2.71033 | -56.53334 | 2026-10-05 17:34:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 48a4eff2-a594-373f-813b-4c9cdb36bf41 | -7.37659 | -72.72657 | 2026-10-05 17:34:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 32c3e0bf-28da-3371-aa87-5ef5b5f782bb | -2.9889 | -57.89622 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5d14e749-f5f4-37fb-9257-19ec06045fd3 | -4.67018 | -54.47497 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3d769553-9265-3ed0-8961-eda7205b864a | -10.85496 | -68.57905 | 2026-10-05 17:34:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4caeca44-56f7-303e-a361-17de58df82fd | -7.36131 | -72.60896 | 2026-10-05 17:34:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1d84c579-957b-33c2-9576-5cd4b7b9f1c1 | -14.30178 | -57.469 | 2026-10-05 17:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2a399405-ebee-322a-aa19-3ad6691d664b | -3.09159 | -54.171 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 894f9666-127b-320a-b5f3-4d3c3b9d36e6 | -3.37628 | -58.20298 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 916e09bf-08b8-3f8a-b3ca-dd212b882bc7 | -7.94691 | -69.92648 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 41befccf-fec9-39a3-9f39-dffa3179d3ba | -7.46836 | -73.38264 | 2026-10-05 17:34:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 41e53b4b-35b3-3f54-a0e5-76349c322e90 | -3.27266 | -59.5962 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e46d98a7-c91d-3aec-a7ca-098e056840c2 | -3.37855 | -58.19449 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 07caf3d5-738c-319b-aae9-3bcbb9ffb546 | -2.93626 | -54.11242 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ac17a399-50e2-3812-add3-5031210c4c6f | -7.35221 | -71.02055 | 2026-10-05 17:34:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8ddc722b-81f2-3ecf-824e-e9d8c0af1acc | -7.66209 | -69.9283 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0b9aabbb-7e68-3387-a82b-c5289b8b94c7 | -3.06691 | -54.16829 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0a017904-5e87-3b4b-b4d1-fd1742ca1e47 | -10.30451 | -63.39614 | 2026-10-05 17:34:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cf3ef3f9-ffd3-3f53-b3d6-0376e72c3dd4 | -7.24206 | -73.10136 | 2026-10-05 17:34:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 554703c5-e81c-33f9-9542-532340cdcc74 | -8.34778 | -70.09881 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e534be06-6c27-38d7-9b75-994fb439632e | -2.93032 | -57.56497 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 69474d09-0ccc-3668-ba12-2def79813c94 | -3.85567 | -59.60986 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cad47ad8-6811-397d-bb5a-17807b713cec | -8.27043 | -71.12019 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| aaf7733e-fafa-355a-8fe9-86db602afca5 | -3.49918 | -57.90031 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 53eb16e8-a055-347b-964f-27aafb525164 | -3.51114 | -59.55538 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5fe6991c-85e8-377a-8c7f-c776eeed6eb2 | -7.94111 | -72.29324 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fa6a2ec3-7130-32d3-98ac-b3d3d696b3af | -12.92101 | -62.18052 | 2026-10-05 17:34:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c8daa6dc-bd3f-31cf-8db2-3785eb5180cf | -2.95988 | -54.14188 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| e05bb636-2338-3933-9053-a5df4b7d1088 | -3.10745 | -58.56337 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 695cd4d3-15e2-3fd9-a495-e992fd4efacf | -6.91115 | -59.26072 | 2026-10-05 17:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f2fbd59c-ca05-34bf-b2f9-50a2d0494797 | -2.98593 | -57.9009 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 12000bcb-f84e-3643-9bf2-be67a135a5a2 | -4.07159 | -55.7693 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dc1c9161-e756-3ed6-8b32-a17c24be6a33 | -3.48422 | -59.58134 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb748170-ddb7-3659-bab2-c599d3c838fc | -4.41089 | -55.1125 | 2026-10-05 17:34:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 85078047-99fc-33c5-aaf5-fdd890fedc76 | -3.59348 | -54.31377 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df0cb246-0cf1-31d2-88f7-1700329021f6 | -5.20524 | -60.1075 | 2026-10-05 17:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 14553627-d280-36ce-8107-1a9e7a36ed43 | -7.93999 | -72.84542 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 81cc3a4a-343a-3436-8f37-88a2ffee0da0 | -3.38279 | -59.42863 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c8b2d000-b62a-3f75-920b-254218769c73 | -7.66642 | -72.42915 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7bb16ca3-c211-357f-b6a1-a6b11db16096 | -7.75862 | -73.07472 | 2026-10-05 17:34:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4c6815ed-4604-32e7-beff-078a1eabd2bf | -3.53763 | -60.41129 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48e095d8-048c-3312-99bb-54bbe0b0b8d0 | -2.95154 | -54.14807 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| e028727c-0db2-3c3b-bd6c-8606fd8ecf8b | -8.08296 | -71.216 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 061f2325-2801-3fe8-895d-17112754d694 | -5.89455 | -55.52925 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4591c5c5-181e-30e1-8b16-9880a7da4090 | -12.10413 | -60.83459 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 584aed3c-ae8a-3cc5-b9aa-0defa3a70fdf | -3.2144 | -57.87984 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 71e84726-b068-3857-9958-3270bcf178e7 | -3.54034 | -55.52081 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fc886846-4c14-3eab-890e-4db6eccf08bc | -1.87703 | -50.04124 | 2026-10-05 17:34:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d858cd63-aa76-31cb-9249-da6a69af453c | -3.58418 | -60.53837 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f71a9549-be38-3662-a7fd-7e794d300442 | -5.96566 | -55.35373 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f9020fb9-d0f5-3136-aa8a-1bf9592515e4 | -3.74419 | -59.613 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72c940b1-b6e6-30d8-84a1-83b99e438a09 | -3.68407 | -61.10427 | 2026-10-05 17:34:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5328f91-87f8-3819-82cf-1c0370d6f260 | -11.22102 | -47.13501 | 2026-10-05 17:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 53e18de6-ebaa-3863-8e64-c24cd5989503 | -3.54356 | -60.51631 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c8b00a8d-c495-39ab-b327-27bc318be568 | -4.61313 | -52.58662 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 37001515-9722-39d3-8f9e-b4ecce7517b0 | -2.94929 | -54.16274 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| ff2c2336-9ccc-338e-aa80-a668e88fb2e3 | -2.99885 | -57.7851 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 5f4b5a6f-71ec-36e5-a91f-3b0be6ebbf38 | -4.12084 | -54.42675 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ecf1abd1-2f91-302b-a0f9-72c04e07d893 | -7.396 | -70.11326 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 866963f4-35de-36f5-ab91-d03b162af001 | -2.94545 | -54.13956 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 167a5b06-4e71-339a-9678-3d6ef3b75f80 | -13.51873 | -61.12532 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1a7f82bc-bfec-3dd3-92c5-418f02da8f6f | -8.19736 | -72.99057 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ac657f75-39ef-346a-abbf-ad18dacb95cc | -3.65014 | -54.05258 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2021b47e-e5ee-3c77-a2a0-85b6bb628c33 | -3.86325 | -61.34454 | 2026-10-05 17:34:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebff1e83-7ca1-38ba-a23e-3ce6e59a6970 | -3.19633 | -54.09358 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 199069c7-0c34-31fb-8e51-7fe1f51786cd | -8.40495 | -70.17256 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4eea60d7-f3ec-3fae-aaa9-711dfa25a634 | -3.55842 | -59.07058 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 28.0 |
| dae4a51e-7aee-31b5-a43a-67eafad9a37d | -10.21627 | -46.67859 | 2026-10-05 17:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c93fd1c3-db1d-3c09-958e-50a0f6e1c277 | -3.5676 | -59.4297 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b9fee990-56b8-3223-9c60-6a72b47211e5 | -3.37513 | -60.68048 | 2026-10-05 17:34:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 74c88c54-8ceb-3627-b543-39ae5561d23d | -6.1684 | -55.37733 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README136.md)
