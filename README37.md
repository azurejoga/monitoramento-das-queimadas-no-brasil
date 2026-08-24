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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4091fde-f093-3587-877d-8bdf7efeb4e7 | -23.88798 | -51.23294 | 2026-08-24 04:49:00 | NOAA-20 | MAUÁ DA SERRA | PARANÁ | Brasil | 4115754 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9565f746-32ca-399e-b59e-a67857926bc2 | -17.09596 | -49.40348 | 2026-08-24 04:49:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfcbfa29-8fe4-306e-9ce3-b1e4ac508881 | -15.67547 | -53.80492 | 2026-08-24 04:49:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dd9c8ca-967f-320c-8206-a408d59b68f1 | -15.26555 | -52.86507 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18f1fa47-faa2-3412-9e7e-8911735c570f | -17.54526 | -42.53987 | 2026-08-24 04:49:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb163c1a-963f-3271-b0bd-20734e25d7b2 | -15.26005 | -52.85655 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cb2426f-3c11-3c00-8b3a-e735c26d0248 | -16.38365 | -51.8256 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a29a2e0d-1bb4-3e69-bc3e-4c0107fc496d | -18.3343 | -43.90923 | 2026-08-24 04:49:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e61d408c-e454-3b8c-a01b-849af5e3f292 | -15.25911 | -52.84129 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1893a8a6-0a39-3147-872e-06d5fd5e5d3f | -15.28396 | -52.81546 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e24cf852-306b-30e2-9680-91a5fd241d36 | -16.06499 | -50.44043 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ae72bdc-c988-32a7-ad5d-990dbe0a2e3b | -14.94271 | -52.67448 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be3f7ec2-8261-300b-873c-cf6235b04ca0 | -17.44074 | -48.84565 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 1e66fb75-020c-387a-9856-22eef2ae0d0e | -15.2645 | -52.80823 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b121ebaa-1fd9-3e6f-85e3-60474148d61c | -16.8556 | -49.44433 | 2026-08-24 04:49:00 | NOAA-20 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39fc1768-5147-3d74-bfbc-8521467b68e0 | -17.42617 | -48.84095 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 028eb371-42b3-3225-93a6-c4da73ce1382 | -15.2585 | -52.84496 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 62359249-1b84-3573-be48-9dcffaedfe8b | -15.28671 | -52.81975 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0b61cfd-2a47-3c0a-9b8b-dccd8c7d6e57 | -16.41015 | -51.83009 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 322cddf1-ee9f-3a27-b52f-d2222b24e1b5 | -15.27047 | -52.87718 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3fdd9c7e-d337-38c9-80fd-9a9317a7485d | -16.87488 | -49.45985 | 2026-08-24 04:49:00 | NOAA-20 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4de99a5c-d664-34df-81c3-996aa012a8e3 | -15.25791 | -52.84862 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fdfaf66a-6b2c-34a6-b394-df7273f0be4e | -15.26735 | -52.85407 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75880dc5-ef16-35b8-a919-faabb550d919 | -16.05373 | -50.42344 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70676a45-6e45-3c09-81f4-314b31b229a2 | -15.35399 | -52.77848 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71c61936-8740-3e67-a905-177d009b36d2 | -15.27106 | -52.87354 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb06475b-eed0-3a2d-9d0c-63505040682e | -14.94665 | -52.6714 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f50b8467-912b-33c4-b98e-fb2c74a5090b | -16.07061 | -50.44897 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee1f0f04-68b1-3bd3-8848-86f23150f470 | -15.26914 | -52.84305 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d55eab4-1f15-3881-8c30-370a6239b852 | -15.26211 | -52.8229 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd3afd1e-480d-3872-878f-4479f600f231 | -22.63816 | -47.81191 | 2026-08-24 04:49:00 | NOAA-20 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43d74239-395f-3e1e-aa36-dd1f5fc3b15f | -16.41631 | -49.91812 | 2026-08-24 04:49:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07052819-1991-38c7-89f2-2ff816858d50 | -23.5181 | -47.36655 | 2026-08-24 04:49:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 62634684-e164-378d-b5da-6d6a373abe0b | -23.00111 | -49.38067 | 2026-08-24 04:49:00 | NOAA-20 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a428eedd-7e78-3604-a588-258d1e6c4377 | -15.78611 | -56.06709 | 2026-08-24 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 536ba172-deb3-3e5c-9a4d-632c7c0bcfdc | -16.41289 | -51.83424 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c3bbf38-3cc4-324e-bd27-c7f274889762 | -22.84823 | -55.13596 | 2026-08-24 04:49:00 | NOAA-20 | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2f87bb79-6530-3d33-ac78-465b54de2b91 | -15.26795 | -52.8504 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b13910f-0c96-3d79-aa39-bc0072090fc2 | -15.35065 | -52.77786 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed07bb98-6183-3ea7-8514-9c19658c0653 | -22.24466 | -54.15732 | 2026-08-24 04:49:00 | NOAA-20 | DEODÁPOLIS | MATO GROSSO DO SUL | Brasil | 5003454 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 708173cf-25ab-354a-b055-ed0f31a6c7ce | -15.51521 | -49.83919 | 2026-08-24 04:49:00 | NOAA-20 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a20a774-5617-34fb-9218-905904a7a06d | -23.82705 | -48.71675 | 2026-08-24 04:49:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5c26b6a-24a4-3407-af94-46927ea580b1 | -14.95274 | -52.6762 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 752e4d7d-21cc-3b08-900a-0727fad2fcba | -22.59475 | -54.97515 | 2026-08-24 04:49:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| af6a0293-72cc-3744-8c46-2bcaf5e9c0d6 | -16.40134 | -51.82122 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dfc5c68-0b03-390d-a2d5-848a478e176f | -16.40885 | -49.92095 | 2026-08-24 04:49:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb591ae3-c31a-35fb-8f8f-baf57c36482f | -16.30576 | -53.1566 | 2026-08-24 04:49:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e7f9f4d-bbbd-34d6-8891-0dae28688d84 | -17.43644 | -48.84694 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 11902b9b-f2ec-381a-b95c-dc11a3d2e399 | -15.35125 | -52.77419 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0821b48e-1179-3647-8d52-12c47debb1d3 | -16.04824 | -48.00585 | 2026-08-24 04:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dbb7266-e2ad-3b43-94ac-741eb5cf4b09 | -16.41287 | -49.91759 | 2026-08-24 04:49:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6d2aa066-75e3-3685-b1b3-1839c391b5f7 | -15.27728 | -52.81424 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a77063d1-100c-3aaf-aa18-277b62c22a6f | -17.4298 | -48.8415 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b763880-2857-35cc-93c3-73c98b232856 | -16.41507 | -51.84198 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d0f9b712-883c-3d87-8035-b4afb8dce99a | -16.3903 | -51.32875 | 2026-08-24 04:49:00 | NOAA-20 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c662b45-14e6-31bb-96a3-06942875ee46 | -23.82309 | -48.71618 | 2026-08-24 04:49:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc2330b2-6c36-31aa-ad36-162d370c7dd7 | -16.42034 | -49.91468 | 2026-08-24 04:49:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14d85f42-02ea-359f-9689-41458499a671 | -16.4256 | -49.92191 | 2026-08-24 04:49:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 026da68c-b23f-3af0-98ae-182583454dd5 | -15.2658 | -52.84248 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9646263e-5052-3574-975d-53e2edc5f6f4 | -15.267 | -52.83511 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 62f32024-de40-3b1d-baa3-8db0b85881e9 | -16.39028 | -51.82672 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f586b969-b281-36bc-bda9-45e2752776ac | -15.24501 | -52.80119 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be720cc8-7812-39d3-b499-9d8e4a79d63c | -16.05713 | -50.44675 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 078f1ae0-bd11-328f-89ac-05b251bb2142 | -16.6735 | -50.161 | 2026-08-24 04:49:00 | NOAA-20 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 456a8530-cedc-3139-8e4a-5706ef9dfa6c | -16.19933 | -57.76321 | 2026-08-24 04:49:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 25ad3954-ff38-3b39-a054-0b19e13030d9 | -15.2646 | -52.84982 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b03c8e05-eca4-33b5-9df4-be030ce1921a | -15.67054 | -53.79218 | 2026-08-24 04:49:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f8f0e05-b807-39e5-9890-08037e79e8b0 | -15.4843 | -49.64969 | 2026-08-24 04:49:00 | NOAA-20 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6026352c-3d51-32f5-bcd1-31343d0956d2 | -14.94331 | -52.67083 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c1ec7fd-f13c-3ce2-a301-5b96d0e05be7 | -17.43711 | -48.84511 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 09f85533-7f0c-35fa-8eed-8ffa406d89f4 | -15.35279 | -52.78583 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5c3040c-96d4-3f10-b33a-f6b1b19790f2 | -16.05319 | -50.44992 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c4024b8b-6b81-3af9-a9da-6fa1ef869419 | -16.7996 | -49.30677 | 2026-08-24 04:49:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4de7862-0af9-3f5d-8a2d-973e08349e43 | -15.26365 | -52.83453 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b580c9e-ca54-34e3-ac6e-a76059758e5c | -16.10868 | -48.56456 | 2026-08-24 04:49:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b8a4132-bbe2-3b50-80c3-8cba2fae249a | -14.94234 | -52.65569 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35bf18e3-296b-34a3-b18a-7e1291da12b7 | -16.85618 | -49.4403 | 2026-08-24 04:49:00 | NOAA-20 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a045a665-36d2-361f-9fba-c35705902da0 | -15.40512 | -55.78112 | 2026-08-24 04:49:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c79a7de9-c505-306a-8540-ed8c415731b8 | -20.91204 | -57.62725 | 2026-08-24 04:49:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 7e03226a-ed98-33b1-bb72-a329757caffa | -15.28062 | -52.81485 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 127ca8d7-fb25-3d3a-95c8-51c6367dba25 | -15.40594 | -55.77649 | 2026-08-24 04:49:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 87ba8ebd-6870-35eb-8ca7-5f3527796159 | -15.25171 | -52.8023 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35ada2ae-1a15-39c0-8227-903b408c3c00 | -16.799 | -49.31091 | 2026-08-24 04:49:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0f31e14-61f1-3ca7-a757-5fb30efe6054 | -16.0605 | -50.4473 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd4f811c-04cb-3d35-8b40-ebed71fdae03 | -29.03456 | -50.64176 | 2026-08-24 04:49:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 72fe94e3-e3c6-39e0-b811-70a1230306f7 | -16.20023 | -57.7612 | 2026-08-24 04:49:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 07391fac-4546-3a80-a595-904fff9f43d6 | -15.25231 | -52.79862 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51052e5c-13a4-3547-80d2-38a75d19e575 | -17.43771 | -48.84076 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 64ed8c59-5363-34ce-8271-3e1180c1a0b9 | -15.27394 | -52.81363 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4d2ad6d-255b-3ef3-af62-53418ccb2803 | -15.24776 | -52.80542 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41266821-3192-3edf-8aaa-bdbe2ca68d16 | -16.41232 | -51.83784 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac5c9069-d3c3-31de-93e0-98b00a42124e | -22.59072 | -54.97836 | 2026-08-24 04:49:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dc489ffb-5920-3d43-95d7-a9204629110c | -15.2689 | -52.86566 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6582830d-0ebe-3afe-abf1-184048b18912 | -25.80309 | -52.57748 | 2026-08-24 04:49:00 | NOAA-20 | CHOPINZINHO | PARANÁ | Brasil | 4105409 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 28999ebf-4166-3dcd-aeb5-ab9acceaa50d | -17.44134 | -48.84128 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 94b9b613-9443-350c-9ae0-22a871260c5a | -16.41572 | -49.92203 | 2026-08-24 04:49:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f6ffcaf-cd86-3257-b951-572edace474f | -17.43344 | -48.84205 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 40588a9f-6176-3c69-987c-e09ceb337c9a | -16.05655 | -50.42767 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26c362ce-7c25-3035-9107-c17ace7b6ad6 | -15.35459 | -52.77481 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59d285b0-9f7e-31da-b8fe-4a6288b1f258 | -15.26065 | -52.85288 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README38.md)
