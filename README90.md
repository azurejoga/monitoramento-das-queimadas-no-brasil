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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1488eb30-f8f9-35f9-99a6-f1b2cdf4b133 | -21.31337 | -47.60263 | 2024-10-07 04:55:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ee1a412-3984-3b64-979c-82624a1b2167 | -21.28481 | -47.3868 | 2024-10-07 04:55:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3afaa67-6983-36dd-9563-e9bf76c98989 | -21.27884 | -47.39518 | 2024-10-07 04:55:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5ca79bf-c0e8-328e-8150-33bf59e40327 | -21.0879 | -47.23149 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cacf2830-30ce-3a55-854d-e74b17db417c | -21.08763 | -47.23402 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de7f5442-e9f8-3e27-ab57-80708b6b7e3d | -21.08736 | -47.2366 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d7a0d0e-96eb-3729-9fbd-931e72eb51f8 | -21.08707 | -47.23933 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78893ef7-cf9d-374c-8c60-e6f3cfa7611d | -21.08284 | -47.23095 | 2024-10-07 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b00bd40-c8ae-3b48-96a7-e3de6fa7927e | -21.08256 | -47.23352 | 2024-10-07 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f0ccce8-2940-369c-876f-c23204d8e6a6 | -21.08229 | -47.23614 | 2024-10-07 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85bbd6fd-2c6a-3369-9965-4a89c1e3b1c8 | -21.082 | -47.23887 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd11d9ca-521c-3b57-88c1-5cdecfeeebe6 | -21.0817 | -47.24172 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 711782d1-2669-3ec7-95e8-b448e101b20c | -21.07777 | -47.23042 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f5bc5e3-0a48-3fa0-8666-84f40a6615b8 | -21.07748 | -47.23314 | 2024-10-07 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ae85867-128d-38ad-9d8a-827672aaf08b | -21.07719 | -47.2359 | 2024-10-07 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae21a39a-6e85-3104-ba21-f72a2df3bbb4 | -21.0769 | -47.23869 | 2024-10-07 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 396c351c-6452-3cb9-a468-dabdb973df53 | -21.07661 | -47.24147 | 2024-10-07 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7feb07d-d847-36c6-a129-09387e3de582 | -21.07271 | -47.22984 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be55b9b8-4d26-30d2-8a98-70139d26b4c2 | -21.07207 | -47.23598 | 2024-10-07 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16e3a4c6-9908-31ef-b0b7-ce52e7d9da03 | -21.07177 | -47.23888 | 2024-10-07 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 917a995b-d4cf-3543-8688-7943ebfd99d5 | -21.07149 | -47.24147 | 2024-10-07 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30d3e120-99b0-3fcb-ac7e-335de8eb8728 | -21.07122 | -47.24406 | 2024-10-07 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d65953fb-b8e2-30c7-9c41-ff42d65e07eb | -21.06666 | -47.23873 | 2024-10-07 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33a6d452-43be-31d3-8a00-c4b863613bd3 | -21.06639 | -47.24134 | 2024-10-07 04:55:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06ec255a-fbc0-349e-a38f-6db6b17bef9e | -21.31282 | -47.60797 | 2024-10-07 04:55:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f0e0ba5b-5fd7-34ca-97fd-ba1979fb6a94 | -21.28387 | -47.39568 | 2024-10-07 04:55:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a636ab1d-a133-31ab-9c8d-47067273d567 | -21.27853 | -47.39819 | 2024-10-07 04:55:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99a782b5-a316-3944-8e5a-7d29d74e3953 | -21.2735 | -47.39769 | 2024-10-07 04:55:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7582d76-37ee-35a1-b340-2d46745bb16a | -21.66454 | -47.7365 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2630b388-d93c-3dcf-bf87-1dc5d1c2d20e | -21.64536 | -47.72884 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 761ce771-7d7c-371a-9b2e-c4376c824ee6 | -21.6022 | -47.7111 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 075889b9-e786-3746-b639-21f176048edd | -21.6004 | -47.72895 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c5a7b8e-cf52-3c42-8254-2f14640c1778 | -21.5999 | -47.71584 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b9967067-241f-32a3-9363-d6b3f905ddd5 | -21.59862 | -47.72767 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f8a58ce4-d3d5-3f46-b445-471451560e1d | -21.59801 | -47.73335 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 29e3642e-895f-3af1-9a9c-68df722df833 | -21.59722 | -47.71098 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b48316e5-9ba8-3a71-9391-f1fca626cea0 | -21.59689 | -47.95656 | 2024-10-07 04:55:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 79f131f4-6a6c-3f69-ba79-0734457e82d9 | -21.59544 | -47.72864 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 5da33c15-8c88-315a-b73c-f00874c12ad7 | -21.59426 | -47.72187 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d59906c4-4726-3968-8829-0d2fd41a8a83 | -21.58777 | -47.94959 | 2024-10-07 04:55:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fab37dbe-0b58-3b69-9b00-b691e5638ba7 | -21.58752 | -47.73804 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 055ae36d-946f-3df3-b2a3-5208b2928bb1 | -21.58496 | -47.71546 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c71c6ae-f26f-3416-a2a9-4ee8a94c37aa | -21.58258 | -47.73751 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 8a6fe76d-f9c7-39fc-b438-f01e759f021a | -21.57824 | -47.73152 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b216bfc-ab2c-3843-a0d6-93e3051eabd2 | -21.57706 | -47.74249 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7e08dacf-be15-348e-b200-6b9798633a0c | -21.57646 | -47.7481 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cf2d72eb-a24f-3704-93be-31014dd0a5de | -21.57386 | -47.72575 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e00ab7bd-b46b-3660-8286-edf231b31ff9 | -21.57274 | -47.73625 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 46b2ed4b-7f34-35d1-8eff-9869f954085d | -21.57033 | -47.75877 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4089861c-c099-351f-8a29-2e6faece8303 | -21.56971 | -47.76457 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 448f4fb5-b74f-318c-beee-88be8a66b1d1 | -21.56954 | -47.71948 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 134ec6c8-03a5-3676-ad36-530a93aebbf7 | -21.56782 | -47.73563 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 32c11c16-6e01-3f6d-86db-4feaa23033ce | -21.56723 | -47.7411 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59534c41-6cf8-3eb7-bcde-e83e82af0e29 | -21.56664 | -47.74669 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9583f932-ce73-3bae-aa4d-2170c8983c77 | -21.56231 | -47.74051 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f27dba6-edcd-3c0f-8ef5-de0402917478 | -21.56172 | -47.74606 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11252c06-eca1-3fc3-a6a6-21cbb1e23b5c | -21.55797 | -47.73439 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7d38ef0c-3358-35c2-95bb-70631f079f70 | -21.55737 | -47.74 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a20b16ac-4a8d-3d73-9b95-5ec6c9834c92 | -21.66516 | -47.73053 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88522090-bbeb-34dc-b9a2-232aac04bf97 | -21.65587 | -47.72392 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2cb8c53f-1726-3b7f-8fe2-e71d2732b92f | -21.64597 | -47.723 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5768d481-8c3d-3519-96ca-53171bb78b67 | -21.63613 | -47.7215 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cd9de8d9-dc5e-3e04-b6b7-d2d29b5bb1de | -21.6251 | -47.73149 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6894f18c-4815-3552-b5bc-7c1b8a52a4c1 | -21.6049 | -47.7159 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee6d01b1-76f8-3ba4-8f54-9752fd3cf391 | -21.59601 | -47.72307 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 68d6a874-4e2e-31ed-a4d5-0957dffc4567 | -21.5949 | -47.71587 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 85fa3270-8c7b-3057-8e4c-58726b7890a6 | -21.59366 | -47.72736 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c8447703-801b-3fc4-83cd-cec59ba165c2 | -21.59357 | -47.95463 | 2024-10-07 04:55:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 18cb1593-9c12-3c3d-85bc-0a4d3b66049b | -21.59307 | -47.73289 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 103ec040-8625-3d38-a4cf-4697e11cae2f | -21.59262 | -47.95021 | 2024-10-07 04:55:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5a04f749-fb06-3ccb-b260-e09b16bf4b81 | -21.59204 | -47.95592 | 2024-10-07 04:55:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 54a87c2d-7293-3eb3-82dc-9aae48c41e6f | -21.59104 | -47.72285 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d60eb2ce-0316-32d6-b88f-f75ef2477e3e | -21.5905 | -47.72817 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 25.7 |
| e48a67e8-d750-3f47-adae-18ada292fe88 | -21.58994 | -47.73374 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 0b884512-152f-3a55-9a45-807ecf8d2b00 | -21.58872 | -47.95403 | 2024-10-07 04:55:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3be9c8b5-40ef-3a1a-971d-6f6cd5e4a71b | -21.58871 | -47.72696 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d12ed9a3-64a0-3ee7-9173-bd28a4b3b320 | -21.58319 | -47.73195 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 72cf6523-77b2-3328-aef4-6e8bc47eb34a | -21.58138 | -47.74875 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 002b8c15-903d-35da-b44f-3921c81e2f8b | -21.57586 | -47.75372 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0c5c615f-f3db-3bcb-815d-0202c36069f0 | -21.57329 | -47.73107 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cf1ad5fb-2093-3658-af6f-1167b43d63bb | -21.56894 | -47.72505 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 118ad060-7774-3090-b929-084a711550fb | -21.56837 | -47.73041 | 2024-10-07 04:55:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e5a758e3-1875-3e44-8026-37afe7b55733 | -21.40383 | -47.80822 | 2024-10-07 04:55:00 | NOAA-21 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad039d38-6ffa-3ee7-9b96-f6834941b8ff | -21.32338 | -47.60281 | 2024-10-07 04:55:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 509334be-d2e1-3110-874f-2d87cbd47e7a | -21.31725 | -47.61356 | 2024-10-07 04:55:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6ba20c9b-46df-3c04-b07f-8de625c65df3 | -21.27821 | -47.40118 | 2024-10-07 04:55:00 | NOAA-21 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 681abab2-1bc0-3102-b669-cdbb0ebd9132 | -21.27319 | -47.40064 | 2024-10-07 04:55:00 | NOAA-21 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 896d2205-93ab-377e-b58d-fa867e4d7387 | -21.32279 | -47.60844 | 2024-10-07 04:55:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 903e3233-c02f-3a2b-b2ad-753e8187901f | -21.3178 | -47.60821 | 2024-10-07 04:55:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3e7ff078-dc7a-302c-8026-e1aaeb40f09b | -21.2892 | -47.39333 | 2024-10-07 04:55:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db94bfed-77c5-36cd-a751-66ab7285b3ea | -21.28418 | -47.39271 | 2024-10-07 04:55:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 136b0402-aa85-309a-bd10-63141e1958f6 | -21.2779 | -47.40411 | 2024-10-07 04:55:00 | NOAA-21 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f8869cd-055d-3620-9ac4-fa8ae506047a | -22.48554 | -48.3692 | 2024-10-07 04:55:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b4d08aa-72d0-3043-8bfd-b12eb6ba285e | -22.48508 | -48.3727 | 2024-10-07 04:55:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29274b21-397c-3b7f-80a0-1175052db03b | -22.48083 | -48.36729 | 2024-10-07 04:55:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f26c325-743f-38e2-adcc-601eb4e48b16 | -22.48027 | -48.37239 | 2024-10-07 04:55:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d6aa27e-f8c9-3518-8fc9-ae5781b89653 | -22.38482 | -48.59079 | 2024-10-07 04:55:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fbb3c279-4b0f-3759-a8d7-a0702c237ace | -22.377 | -48.59997 | 2024-10-07 04:55:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6dfa8a65-d32b-30d1-88cf-b9c35bd22d2a | -22.37487 | -48.59462 | 2024-10-07 04:55:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7c2be119-002f-32c8-aa19-ceda4bb86dfe | -22.37431 | -48.59997 | 2024-10-07 04:55:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |


[Clique aqui para ver as próximas entradas](README91.md)
