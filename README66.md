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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52eb32d2-4975-3ce6-afb8-d25e4f6598d1 | -19.5465 | -56.6983 | 2024-10-23 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 192.6 |
| fce3f755-afa6-3b9d-b88f-c9ce5417e71d | -19.5276 | -56.6381 | 2024-10-23 12:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 104.0 |
| 847533ee-8282-3a0d-ada4-c7c10f891652 | -12.9166 | -42.2767 | 2024-10-23 12:16:18 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 223.6 |
| 7d42d141-3d45-3da4-947c-f37e3f21a62d | -12.9161 | -42.301 | 2024-10-23 12:16:18 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 251.2 |
| fc5a1398-7de8-3a2b-b96d-b3d63c67b454 | -17.764 | -57.5526 | 2024-10-23 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 898fe64a-0f11-39bd-858e-6243de93ba30 | -17.6868 | -57.4593 | 2024-10-23 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 152.3 |
| bd61b8ed-0ea2-30e4-9657-fb5a52dac14b | -17.744 | -57.5756 | 2024-10-23 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 162.4 |
| 80d1e91e-ab3e-3117-a17d-1e4103d9ecf0 | -17.7637 | -57.5732 | 2024-10-23 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 169.7 |
| 70a66ec2-610b-3622-a086-9d11c1439dd6 | -17.6671 | -57.4616 | 2024-10-23 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 8836d4e5-99e5-3d41-8593-407d2a4504fc | -17.7848 | -57.4885 | 2024-10-23 12:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.1 |
| 15091fae-cdeb-326a-8cff-08dc060064b7 | -11.1157 | -48.6343 | 2024-10-23 12:26:09 | GOES-16 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 35f48ad2-2ca1-32aa-8eca-10ab99df9d1c | -12.9166 | -42.2767 | 2024-10-23 12:26:18 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 177.4 |
| a093de72-75e3-39aa-8eef-b54f4db4a43f | -12.9161 | -42.301 | 2024-10-23 12:26:18 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 186.2 |
| b7d63f53-8889-3493-a9d7-293fd9bee6e2 | -17.0184 | -57.5178 | 2024-10-23 12:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| c7f5b9dd-aea5-3800-81de-a48b70b4685f | -17.2766 | -57.3032 | 2024-10-23 12:26:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| b1917984-a96f-3f11-9d49-974ca6778db1 | -17.7637 | -57.5732 | 2024-10-23 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.5 |
| 4a535aa6-cfac-30b1-9566-7045146ec8a3 | -17.6868 | -57.4593 | 2024-10-23 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.1 |
| 5db46770-5975-3ba5-a422-0a4c62cd8014 | -17.747 | -57.3903 | 2024-10-23 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 9eaacf56-adc6-3cac-99cd-c06d01795553 | -17.7848 | -57.4885 | 2024-10-23 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.1 |
| e8aebbea-bd1e-3c12-9e37-81c4f40feeca | -17.6871 | -57.4387 | 2024-10-23 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 3cb2b052-63b5-3297-8f06-96603c8a2e86 | -17.764 | -57.5526 | 2024-10-23 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 7aef94b4-91ad-395e-a8c0-eacaf5d00568 | -17.7065 | -57.4569 | 2024-10-23 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.5 |
| a9335b7d-4398-3bf8-a68c-7f7ef75e692b | -17.744 | -57.5756 | 2024-10-23 12:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.7 |
| a5fe622d-4dab-3396-8fe2-6284d6b66f28 | -18.2637 | -56.0603 | 2024-10-23 12:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 8f3b6458-982a-37f4-a177-6ffd1b9fd223 | -12.9166 | -42.2767 | 2024-10-23 12:36:18 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 141.7 |
| 79e86442-b110-3197-bdb3-b9d506199f41 | -12.9161 | -42.301 | 2024-10-23 12:36:18 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 152.3 |
| fc5c9829-7648-3800-b566-d909bff4eef0 | -15.9077 | -51.7598 | 2024-10-23 12:36:36 | GOES-16 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 43dce54e-9449-3b1d-b3fe-00078defac51 | -15.9081 | -51.7383 | 2024-10-23 12:36:36 | GOES-16 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 205e7061-ad90-398e-a353-6e94d91b1497 | -17.0184 | -57.5178 | 2024-10-23 12:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.0 |
| 0fe9c36f-0b9a-3400-bbfb-b8e5b4cf5bdb | -17.2766 | -57.3032 | 2024-10-23 12:36:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.8 |
| 6d3fc97d-ca71-30fd-ac49-70e81ef93b6f | -17.2769 | -57.2826 | 2024-10-23 12:36:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.7 |
| bbdd888d-c4a7-36e8-b17b-6d0ae81f996d | -17.2573 | -57.285 | 2024-10-23 12:36:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.1 |
| 20ed03ba-c6ed-3990-8ede-5b562f9fc5db | -17.257 | -57.3055 | 2024-10-23 12:36:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.4 |
| c446a47b-3d33-3d9c-9cf5-93e9f09dbb58 | -17.764 | -57.5526 | 2024-10-23 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 9168bb9f-ef44-3577-bac1-a20791db8b9f | -17.6871 | -57.4387 | 2024-10-23 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| d24f8b61-6486-3159-af1f-afba27955891 | -17.747 | -57.3903 | 2024-10-23 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 06af4516-0708-3193-bc2b-2953ef758c22 | -17.6671 | -57.4616 | 2024-10-23 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| fdd4706c-5693-3b8c-8c62-14ec9af80dd3 | -17.6868 | -57.4593 | 2024-10-23 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 152.4 |
| c44757b5-33e4-36d6-8c90-e5dffaa9022b | -17.7637 | -57.5732 | 2024-10-23 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.4 |
| 53ea5611-8fd1-3ab2-94fe-be8e18670aa2 | -17.744 | -57.5756 | 2024-10-23 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.5 |
| 78a0aa1c-4247-3f8d-878f-3a8f9dc12c96 | -17.7065 | -57.4569 | 2024-10-23 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 59cf4a05-de5d-3b95-be41-94fc912522f7 | -17.6865 | -57.4798 | 2024-10-23 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| ce108d72-4003-36e9-b99c-453e13787e8b | -17.6674 | -57.4411 | 2024-10-23 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 98af0897-5533-357b-8937-782cc141292f | -17.7848 | -57.4885 | 2024-10-23 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 136.6 |
| cf9aaea1-80c1-31eb-926e-560b3bfb945c | -17.7273 | -57.3927 | 2024-10-23 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 3791ee20-eb68-3b32-b015-e02506f385ce | -18.2637 | -56.0603 | 2024-10-23 12:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.7 |
| d398708f-87aa-30e6-9ce2-2441b4792454 | -11.1157 | -48.6343 | 2024-10-23 12:46:09 | GOES-16 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| af81053d-01a3-3631-83f5-8489d1b007a5 | -12.9166 | -42.2767 | 2024-10-23 12:46:18 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 42cdbf11-6dd1-3815-93f1-75066be84b74 | -12.9161 | -42.301 | 2024-10-23 12:46:18 | GOES-16 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 99.2 |
| c8de94d3-ac6d-34b2-9e97-a7bdef59262a | -15.9077 | -51.7598 | 2024-10-23 12:46:36 | GOES-16 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5094dd57-c2d1-3f8d-9667-2382a9f45395 | -17.0184 | -57.5178 | 2024-10-23 12:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.3 |
| 286a6e65-b5e5-35e3-988a-4b3b8f16a203 | -17.2769 | -57.2826 | 2024-10-23 12:46:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 246.5 |
| fa664e98-4171-305f-9b80-8f24a0ba0c55 | -17.2766 | -57.3032 | 2024-10-23 12:46:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 207.9 |
| d3cec22d-72d9-353b-bbe7-f55cc62ac496 | -17.2573 | -57.285 | 2024-10-23 12:46:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 149.1 |
| 84ab5ee1-8187-3f07-b04f-e065ebdd7cbe | -17.257 | -57.3055 | 2024-10-23 12:46:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.8 |
| bc52e0b5-4a7f-3295-b097-2b396c1e662c | -17.6674 | -57.4411 | 2024-10-23 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 3ce571aa-e85c-32ea-b479-c0505abec8f7 | -17.7848 | -57.4885 | 2024-10-23 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 148.0 |
| de953171-8bda-3761-bc08-1c6273d2d6a2 | -17.747 | -57.3903 | 2024-10-23 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.2 |
| 89f7075e-5fa0-30ad-8cd9-2e9a606641cc | -17.6671 | -57.4616 | 2024-10-23 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 9b38bd24-e3c8-3d7a-b9c2-6783c34baf9b | -17.6868 | -57.4593 | 2024-10-23 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.1 |
| 5e4697b6-742b-35be-93f7-160a48972bcd | -17.7269 | -57.4133 | 2024-10-23 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| fb791066-1e2f-3407-9956-48169044ba67 | -17.7637 | -57.5732 | 2024-10-23 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 149.5 |
| 8be3f537-ed05-3adc-84e4-56e9e4aa9d6c | -17.744 | -57.5756 | 2024-10-23 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 138.6 |
| 4d37ed8d-9482-3b87-895f-cb9906ef3a45 | -17.7065 | -57.4569 | 2024-10-23 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| dd115abf-c68a-3b7c-a6a9-da605a5c2912 | -17.6865 | -57.4798 | 2024-10-23 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.5 |
| 5e202f0e-7ed2-3e9e-b515-0f7d8c07a04c | -17.6871 | -57.4387 | 2024-10-23 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 47aa723e-7e77-396d-84ae-5d9a8e0d779e | -17.764 | -57.5526 | 2024-10-23 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 2dc139df-fc94-3b00-af49-8995bfb2b27d | -17.7273 | -57.3927 | 2024-10-23 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| a656a3f0-03b3-334a-bd9a-cbc57726b337 | -18.2633 | -56.0812 | 2024-10-23 12:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.1 |
| 2777a23b-a3ec-3eed-a541-48fecb6632e2 | -18.2637 | -56.0603 | 2024-10-23 12:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 152.3 |
| 1724dbf9-3cd5-3051-bc4e-54e7fb1c8a4e | -18.2836 | -56.0576 | 2024-10-23 12:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.7 |
| f5dd05ca-e782-3a29-b739-d653973042a0 | -0.952 | -47.6899 | 2024-10-23 13:05:12 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| bf14665b-e95d-3613-94a3-77f219c34b1d | -15.9081 | -51.7383 | 2024-10-23 13:06:36 | GOES-16 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 555342f7-3cf5-3992-afe6-25cf756ef079 | -15.9077 | -51.7598 | 2024-10-23 13:06:36 | GOES-16 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 746f2e66-33cf-3365-a23d-300813ed9685 | -17.0188 | -57.4973 | 2024-10-23 13:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 228abae3-5c28-3f19-a9c3-df4a110a60a8 | -17.0184 | -57.5178 | 2024-10-23 13:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.1 |
| 48beaf7e-d216-3277-9979-0a06d0acad35 | -17.2376 | -57.2873 | 2024-10-23 13:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 4789796a-8eb3-3adf-82af-a662dd2e8ea1 | -17.2373 | -57.3079 | 2024-10-23 13:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| b6dcbedb-dc73-38ec-b63e-4aeebe82f3f5 | -17.257 | -57.3055 | 2024-10-23 13:06:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.0 |
| 258f45a4-cc4d-315a-8dad-9f18f919f08e | -17.2573 | -57.285 | 2024-10-23 13:06:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.4 |
| 895531df-021f-39c0-aad5-56994c1d102b | -17.2766 | -57.3032 | 2024-10-23 13:06:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 205.8 |
| 4fc7ce2b-da1a-39a1-8266-238b17ec73b1 | -17.2769 | -57.2826 | 2024-10-23 13:06:44 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 298.3 |
| a72fd366-d05c-3aad-bee3-fe5bba123752 | -17.764 | -57.5526 | 2024-10-23 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| d981a7fd-430b-3983-bf01-3c2e139cdd25 | -17.744 | -57.5756 | 2024-10-23 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.7 |
| 3c975a30-3feb-3872-a2c3-3f42b330574f | -17.8045 | -57.4861 | 2024-10-23 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.5 |
| a2d26277-dc4d-3823-96f4-7ddb9559a941 | -17.7637 | -57.5732 | 2024-10-23 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 215.5 |
| 8c4e4bd6-c9a9-35d1-bb4d-71e078e7d44b | -17.7269 | -57.4133 | 2024-10-23 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 33330322-20a1-35f9-970d-99b6040f025c | -17.747 | -57.3903 | 2024-10-23 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 167.7 |
| d904abb5-3c27-3f86-8f5c-fcd5eb307998 | -17.7273 | -57.3927 | 2024-10-23 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 898be34a-ddf3-39e8-bc0a-4da553e2d284 | -17.7848 | -57.4885 | 2024-10-23 13:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.0 |
| efc939c2-4a22-34fd-a3ad-4dedeb83a017 | -18.3004 | -56.2222 | 2024-10-23 13:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| b3f6aacd-2edc-3617-9afd-aabea0661b4f | -18.2836 | -56.0576 | 2024-10-23 13:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| aeb32385-3a42-3168-9757-f7ba5ea9a2a0 | -2.3255 | -46.2385 | 2024-10-23 13:25:19 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 22a6be5b-e8fa-3538-9d2f-6462c20a7e0b | -3.8329 | -42.4533 | 2024-10-23 13:25:28 | GOES-16 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 213.2 |
| a90a8c27-fd10-390f-9b76-154eeb89b646 | -11.1157 | -48.6343 | 2024-10-23 13:26:09 | GOES-16 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 8244ef72-59ad-3510-b1eb-64df513e4d23 | -12.9938 | -47.164 | 2024-10-23 13:26:19 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 7f031e71-4d29-35e9-913f-60eeb1eb1130 | -15.9077 | -51.7598 | 2024-10-23 13:26:36 | GOES-16 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| fb4b19a2-5ed8-3b9a-aaf7-241e37e9da73 | -17.0213 | -57.3333 | 2024-10-23 13:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 23f9eee3-2a69-3905-8a72-eddb50d71ca3 | -17.021 | -57.3538 | 2024-10-23 13:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 146b245a-48c0-34ce-bea2-a620b6f4360b | -17.0194 | -57.4563 | 2024-10-23 13:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |


[Clique aqui para ver as próximas entradas](README67.md)
