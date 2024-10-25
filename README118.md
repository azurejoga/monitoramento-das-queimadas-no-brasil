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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7178ade6-569b-3c63-ad1c-adab7755320b | -23.82829 | -55.31854 | 2024-10-25 12:57:00 | TERRA_M-T | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 4ffc811b-8725-3615-80a0-084771613a86 | -23.8224 | -55.29514 | 2024-10-25 12:57:00 | TERRA_M-T | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 9f5e6c8b-8558-3cc0-9347-951883039a7f | -23.81821 | -55.28786 | 2024-10-25 12:57:00 | TERRA_M-T | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 9399838c-5368-36e6-a779-221402af1aa7 | -3.5273 | -43.6134 | 2024-10-25 13:05:25 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| f4e2755f-7bb6-3bf5-bc83-dcceebf5f395 | -3.6826 | -42.5789 | 2024-10-25 13:05:26 | GOES-16 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| b694124e-5efb-39e3-86c9-40da2c1f38e4 | -12.5272 | -43.3782 | 2024-10-25 13:06:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| b391033e-a1d8-3bcf-9a6d-5581089b4086 | -12.9975 | -43.0341 | 2024-10-25 13:06:18 | GOES-16 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 153.3 |
| 6c7f4634-2db1-3dba-ab41-9ed8e1aad587 | -16.554 | -57.2237 | 2024-10-25 13:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.1 |
| c2382898-f0e6-3805-a20a-fffa02747013 | -16.9596 | -57.5245 | 2024-10-25 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| fd1b8cc3-ad32-3d75-9bb9-7407d9e627fd | -16.9211 | -57.4881 | 2024-10-25 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 22d56c2a-3774-3198-861d-d1d2a5fb8977 | -17.039 | -57.454 | 2024-10-25 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 83ccae22-9b56-35d4-a4ab-4b9a8c43add7 | -16.9792 | -57.5223 | 2024-10-25 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.1 |
| 103b15b3-7cba-33e5-afe9-1e53d15b43fe | -16.94 | -57.5268 | 2024-10-25 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.3 |
| c995d133-fe0e-38cc-b230-b6c0b05212bc | -16.8983 | -57.6949 | 2024-10-25 13:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 1e26aa5f-3a41-3c9e-be26-2d8387869db1 | -17.0786 | -57.429 | 2024-10-25 13:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| f6315256-3a2a-3870-980b-f26f79335f56 | -17.0789 | -57.4085 | 2024-10-25 13:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.8 |
| eb512d4d-1103-33fa-85bf-706fc3700885 | -17.2537 | -57.5108 | 2024-10-25 13:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| b98a8de0-73a9-3a75-aa2b-2999b3b5437a | -17.6888 | -57.3357 | 2024-10-25 13:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| c40ca737-6189-3983-8fdd-b019325639e9 | -17.8628 | -57.5407 | 2024-10-25 13:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 0285181c-f9ad-377b-89d6-98d0df2eb704 | -17.8825 | -57.5383 | 2024-10-25 13:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 7a466bdb-5731-38ed-aa82-fe1a90dcf41a | -17.8222 | -57.6072 | 2024-10-25 13:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.1 |
| d08ba365-7e2a-3655-8d8c-b868027e0cf3 | -18.2641 | -56.0394 | 2024-10-25 13:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.7 |
| 7dffe08a-931f-344a-8416-dddcbf2dbfd8 | -18.2637 | -56.0603 | 2024-10-25 13:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 004cccea-f812-3367-b3f4-f4e147cd5efa | -18.2645 | -56.0184 | 2024-10-25 13:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.8 |
| 72adb577-080e-324a-a291-1b4e2f6105b7 | -18.3 | -56.2431 | 2024-10-25 13:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 792356e9-75da-3640-906b-a987de87bf2d | -18.3398 | -56.2377 | 2024-10-25 13:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 8db60472-12a9-30fa-ad47-ed8cc091fe19 | -19.641 | -56.9988 | 2024-10-25 13:06:55 | GOES-16 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 68.5 |
| 7e4f1b3a-71b6-3fc0-bd4a-884dd509762e | -19.6407 | -57.0197 | 2024-10-25 13:06:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.3 |
| a2559ad9-0ee1-3844-abfa-c03069a6303d | -3.5273 | -43.6134 | 2024-10-25 13:15:25 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 38e1c1a9-d6d9-3072-85c7-e872426088cc | -12.5272 | -43.3782 | 2024-10-25 13:16:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 79883c9e-e36d-37ce-ad8a-848bb3c2f9fa | -12.9683 | -42.5821 | 2024-10-25 13:16:18 | GOES-16 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 01e2e9f3-aa13-31f2-a5d5-0b5fa9aad5de | -16.554 | -57.2237 | 2024-10-25 13:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.1 |
| 2ba980f8-f595-3d7a-a08f-f7ef72fd6585 | -16.8983 | -57.6949 | 2024-10-25 13:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 802847f0-27f8-3298-b204-7974b58e4b61 | -17.0184 | -57.5178 | 2024-10-25 13:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 70ee6282-9a5c-304a-960a-8f6c7fa77d82 | -17.0188 | -57.4973 | 2024-10-25 13:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 12accf47-0443-3507-9692-0bb3dbb29c9d | -17.0191 | -57.4768 | 2024-10-25 13:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| d6baf560-70a3-3467-b7b6-360bbd68c38c | -17.039 | -57.454 | 2024-10-25 13:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 11ed311b-67dd-30e7-8fce-675cb9fb1837 | -17.0786 | -57.429 | 2024-10-25 13:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| a75d1f34-c1aa-3643-953b-d165afaf64f8 | -17.0789 | -57.4085 | 2024-10-25 13:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 192.1 |
| 7165af22-14e7-32b7-9b69-ce9caf89d69e | -17.2537 | -57.5108 | 2024-10-25 13:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| f7842919-251b-316d-b23b-6544bd048369 | -17.8226 | -57.5866 | 2024-10-25 13:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.3 |
| e9ac54d2-7ee6-3611-9366-31cbd38d92ba | -17.8628 | -57.5407 | 2024-10-25 13:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.5 |
| fb14c3b3-7f87-36b4-87bf-9e066fad6f4e | -17.8624 | -57.5612 | 2024-10-25 13:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| f5c578f3-82ff-3fcc-9c72-ab75dbf73047 | -17.8825 | -57.5383 | 2024-10-25 13:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 173.4 |
| 5d3199a3-dffc-3901-aae3-27b3ddf495b1 | -17.9019 | -57.5564 | 2024-10-25 13:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.8 |
| d0c59155-c9b3-359f-b0a3-9528e35e1ef6 | -17.8222 | -57.6072 | 2024-10-25 13:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.7 |
| 373e2d60-6553-332b-b71a-d141aae9bb08 | -17.9023 | -57.5359 | 2024-10-25 13:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 6928507f-941a-3a29-8079-ae4c3729c1e4 | -18.0455 | -57.2299 | 2024-10-25 13:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.6 |
| e9145ad4-2d37-3eb7-b5e0-8c83dee73cc9 | -18.2832 | -56.0785 | 2024-10-25 13:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 0009f59d-3672-3a49-8177-6fe3eabbce02 | -19.641 | -56.9988 | 2024-10-25 13:16:55 | GOES-16 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 72.5 |
| cf7a8655-9550-338c-8759-4c12ed2eac5b | -19.6611 | -56.996 | 2024-10-25 13:16:55 | GOES-16 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 0e4cc44d-b513-3e4f-a701-6f3dddf5a372 | -19.6407 | -57.0197 | 2024-10-25 13:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.7 |
| f0774456-3eb5-3d3f-b1bd-d12bd402b40b | -12.9683 | -42.5821 | 2024-10-25 13:26:18 | GOES-16 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 0db98f51-5b6a-34f2-968f-20b374cd1f4a | -16.8591 | -57.6993 | 2024-10-25 13:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 5869bc7b-b3ed-38a0-8db2-632e899dd638 | -16.8983 | -57.6949 | 2024-10-25 13:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.4 |
| cbe42d35-2c93-371a-b7e0-3f85801ad2af | -16.9179 | -57.6926 | 2024-10-25 13:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 74504318-1202-35a9-929b-14e37fc68d9b | -17.021 | -57.3538 | 2024-10-25 13:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| 95a2c4e5-c68f-3836-a162-51cb98e5cc4a | -17.2537 | -57.5108 | 2024-10-25 13:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 1f3cec22-9e68-3e5f-b6fc-9af646aa4148 | -17.8028 | -57.589 | 2024-10-25 13:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.6 |
| cd4105fc-a60d-392e-aa7a-f7c7c386e5cd | -17.6888 | -57.3357 | 2024-10-25 13:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 6f372f76-b5f8-36f6-8657-f3879e8996fa | -17.8222 | -57.6072 | 2024-10-25 13:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.4 |
| 38feb99b-d64d-3894-8252-d876c7179cf5 | -17.8226 | -57.5866 | 2024-10-25 13:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.6 |
| f6157cc6-365c-305e-8e05-b31d6f6f69f3 | -17.8624 | -57.5612 | 2024-10-25 13:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| a4d3e762-0ba6-3841-885a-c57bf63d5238 | -17.8628 | -57.5407 | 2024-10-25 13:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.7 |
| b009e1e8-2144-3ba6-be6b-99c1bdac2861 | -17.8822 | -57.5588 | 2024-10-25 13:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 577405c5-2f4e-3ca1-8708-bf179a7239cc | -17.8825 | -57.5383 | 2024-10-25 13:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.0 |
| 7a6b9941-3359-3dad-b29b-4ca534860fc1 | -17.9019 | -57.5564 | 2024-10-25 13:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.7 |
| a47ed9da-7ced-3ee7-b4e2-1a80a201743c | -9.39947 | -65.57818 | 2024-10-25 14:29:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 664882dc-a566-3a5a-bc98-cf981c29c44d | -9.09179 | -65.6413 | 2024-10-25 14:29:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 3e0b84c8-04e3-39e9-9910-05b52e341a70 | -9.00337 | -67.01745 | 2024-10-25 14:29:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 26bb4bfb-6a7f-39a4-b98e-c5b743f2419b | -9.00308 | -67.36282 | 2024-10-25 14:29:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 109eb3b1-ea63-33de-9f83-f1e7dc9855db | -8.99738 | -67.0101 | 2024-10-25 14:29:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.3 |
| dcd39532-8ff4-3349-90f4-9841cc4e064a | -8.99445 | -67.03338 | 2024-10-25 14:29:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.3 |
| ac126f0d-8312-3700-8761-c2b484714efa | -8.5129 | -64.01675 | 2024-10-25 14:29:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| a07f5eee-052a-3358-8a56-a014aa091f08 | -8.50235 | -66.98967 | 2024-10-25 14:29:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| f1bba43f-fa24-3fd9-a83f-c81da2b21519 | -7.87827 | -63.73561 | 2024-10-25 14:29:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 5f50b973-2348-3cac-abf8-56988ba5c247 | -7.87724 | -63.73021 | 2024-10-25 14:29:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 61d72802-8681-3419-9930-4ff85c1d6425 | -7.65337 | -67.32018 | 2024-10-25 14:29:00 | TERRA_M-T | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 2c457d1c-edaa-3db0-a142-7cb23ba6bebb | -7.52971 | -63.62844 | 2024-10-25 14:29:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 5555037a-eccc-33cb-b180-468679d4ad22 | -7.52906 | -63.62351 | 2024-10-25 14:29:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| d184a88b-dd20-3fc7-85f2-21803842ece0 | -7.49801 | -63.74833 | 2024-10-25 14:29:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| f0dd0a2e-123e-3c94-b418-32f7ca681d53 | -7.49655 | -63.74331 | 2024-10-25 14:29:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| aa0896a0-98e1-33fb-b506-0d52dd06c85b | -7.45732 | -64.46333 | 2024-10-25 14:29:00 | TERRA_M-T | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 4aea9eaf-3418-3816-8270-7efd353bcfab | -7.32495 | -72.75974 | 2024-10-25 14:29:00 | TERRA_M-T | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3647d0a7-fd9d-305a-bbe5-4ea5cad5ac62 | -6.56216 | -69.95724 | 2024-10-25 14:29:00 | TERRA_M-T | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| bcb62fcd-7dbd-3a51-aabd-df3158f536a9 | -2.95477 | -65.11063 | 2024-10-25 14:29:00 | TERRA_M-T | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 57ecac4d-c6ce-3e20-bb5b-aa2a9520b3bd | -2.52995 | -66.18906 | 2024-10-25 14:29:00 | TERRA_M-T | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f4b06877-ff97-3550-ae27-8c4f4b9c5175 | -6.26708 | -35.46354 | 2024-10-25 15:09:00 | NOAA-21 | SANTO ANTÔNIO | RIO GRANDE DO NORTE | Brasil | 2411502 | 24 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a046018d-77d6-3fcf-8d53-e52fac738ae9 | -5.96385 | -35.15911 | 2024-10-25 15:09:00 | NOAA-21 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 44d5ad8d-adb4-36e6-85fe-be6944fe61de | -6.90192 | -35.50518 | 2024-10-25 15:09:00 | NOAA-21 | CUITEGI | PARAÍBA | Brasil | 2505204 | 25 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 521bfa2f-4e68-3fba-98f6-48d2df4e4249 | -6.90189 | -35.50395 | 2024-10-25 15:09:00 | NOAA-21 | CUITEGI | PARAÍBA | Brasil | 2505204 | 25 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 883c8861-b097-3398-b82f-c78abb733e96 | -6.48332 | -35.69285 | 2024-10-25 15:09:00 | NOAA-21 | ARARUNA | PARAÍBA | Brasil | 2501005 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ec9147b3-50ba-3320-aa5d-b2e7e00dec51 | -7.62387 | -34.9216 | 2024-10-25 15:09:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| a7eeebe4-985b-3a89-9fe7-946a15b2f500 | -7.59409 | -34.87097 | 2024-10-25 15:09:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| df2c8c16-ccc7-3e65-8974-32bc9b34b3fc | -7.55582 | -34.95105 | 2024-10-25 15:09:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b3489e2c-9c93-3cc7-ae99-752c41f92345 | -7.48992 | -35.10992 | 2024-10-25 15:09:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| d730a183-e4d7-3625-bbb7-32e92aab2b16 | -7.48862 | -35.11346 | 2024-10-25 15:09:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 21e953f0-4d7a-34f6-82fb-d12e38f523ef | -7.19214 | -35.24406 | 2024-10-25 15:09:00 | NOAA-21 | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 7c5d7457-2065-3302-b60d-4a9d0dbd7989 | -6.98909 | -35.27829 | 2024-10-25 15:09:00 | NOAA-21 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 6593c409-44ef-3831-b7ed-4fe43bdaf820 | -6.9845 | -35.27856 | 2024-10-25 15:09:00 | NOAA-21 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Mata Atlântica | 29.5 |


[Clique aqui para ver as próximas entradas](README119.md)
