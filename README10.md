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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab24e717-0370-3e2c-ac6c-b07eea8c4cc9 | 0.09309 | -60.51655 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0951cda-daa9-3656-b170-3281d5f51a68 | 0.91849 | -60.53127 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16c49138-4dcd-347a-b386-b3d3047bc3c0 | 0.67072 | -60.3612 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c799ec7b-f846-3b62-af32-93a23640c6b1 | 0.31603 | -60.44233 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9c4f727b-d246-36ef-8eeb-b85cc98e07f4 | 0.30039 | -60.45204 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b32f46a7-fa63-36fc-8866-fcfacaeb418f | 0.04288 | -60.98442 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b59c5c0d-65e4-3aed-828a-58d02924c709 | 1.08237 | -59.24745 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dacf745a-3284-3ccf-b87f-3b18341a3f54 | 0.15063 | -60.48937 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef1b71cc-39b2-320c-9a00-957d24c9fb55 | 1.33738 | -60.06657 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69964b07-5742-3def-b658-98b58aec6a66 | 0.04171 | -60.97714 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 637d7aec-ab1b-3354-b726-4c45adc27100 | 1.06257 | -59.25054 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dfa26ea-380e-308d-8db0-3d6af7a12a1e | -10.40709 | -52.94039 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cb284769-ceca-3366-a1f2-5b91923ff758 | 1.05984 | -59.49022 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 101d4f47-4ade-3954-8002-47296bad6226 | 0.48765 | -60.51359 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a2806f8-7fb8-37ea-8873-c725068d6dd6 | 1.2114 | -59.97773 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbafbfa2-0a43-3b74-b3a7-1445da95bf8e | 0.4938 | -60.50896 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df8e65c1-b0c9-3b69-879b-25e988163e51 | 0.49716 | -60.50843 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ee36a8c-2d78-3496-8130-d156892a250e | 0.0528 | -60.97535 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8d2f0ee0-6bd8-3e43-9631-799d8716bd2c | 0.05848 | -60.98944 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdbf52a7-a186-35ce-bda8-4c6856ccc0f6 | 0.06245 | -60.99258 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6ec414d-cb35-3cba-8a8a-0a68be13266b | 0.05364 | -60.98643 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 49e459a6-bd3d-3a76-a069-6fe27561c316 | 0.04793 | -60.97245 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 4c30fd20-c9d0-3ab7-badc-6c54d2c2d65c | 0.96782 | -60.52752 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a76d5107-3ab4-32d8-892d-32778f3c3b21 | 1.03512 | -59.46234 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8865adb-a795-3d58-95dd-e736bdea8bb9 | 1.11273 | -59.20016 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11b01368-4c70-33b2-9841-cf2f4930ed0f | 1.35741 | -60.06345 | 2026-03-04 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbcfaf71-ac11-34b3-97e2-cb36912d5cee | 0.92972 | -60.53682 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b831f03a-203d-321f-83b0-0840a74e7c54 | 0.07888 | -60.65716 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d58c7ace-a810-3472-aa63-b7142c646172 | 0.73134 | -59.90648 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8cc66aff-77d2-36b5-97a6-8bcca654231c | 0.65173 | -60.37141 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c331f6a-7e33-3289-b1ef-a4eb9b69b18e | 0.07144 | -60.54518 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3169ce55-c1a8-38c1-bd34-f84c86c7727a | 0.9673 | -60.3921 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 60a88011-01ba-324d-ac4a-27631e2afcde | 1.02333 | -59.79671 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a51f929-1415-3e0d-a349-40dd35c920d0 | 0.04006 | -60.98862 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| b8ea381e-4385-3caa-87d9-06f8ff9ea4a9 | 0.06016 | -60.97795 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c676cf7-b0d9-3df2-aef6-d8befbc42a50 | 0.05733 | -60.98211 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8012d11e-1aa7-3ea4-baa3-8b511da01223 | 1.11219 | -59.19674 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aed75762-34e4-359b-9315-94344e31c6cc | 0.65127 | -60.00098 | 2026-03-04 05:25:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71423a8f-2bfe-31a0-8623-5600246bf227 | 0.1767 | -59.429 | 2026-03-04 05:25:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fd90b87-59df-3ccc-8bf0-ed98880e28a5 | -0.14672 | -60.75838 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a975996-ac03-3713-8e04-0f92a8c8f55b | 0.04065 | -60.99228 | 2026-03-04 05:25:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 1f5d6faf-efaf-3646-8997-25a7d33ea7f1 | 0.87597 | -59.40324 | 2026-03-04 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79ae58a8-4db4-351e-8b0c-a0ba192e5ab3 | -20.55043 | -49.27403 | 2026-03-04 05:27:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0ddd8ff5-7234-3be4-9e57-753ea2010081 | -20.02353 | -50.68959 | 2026-03-04 05:27:00 | NOAA-20 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 30ede56c-79a0-3bfd-b2b4-954d690b997f | -13.97906 | -53.45795 | 2026-03-04 05:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 4c2f9172-55f5-39a3-adad-6503c9a309c3 | -16.43736 | -52.47755 | 2026-03-04 05:27:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d377de83-2175-312c-970b-8aae74bc910f | -16.65568 | -54.27006 | 2026-03-04 05:27:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 0a69a6f4-dc6a-39e3-98b9-508324840edc | -15.31701 | -52.11823 | 2026-03-04 05:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 68fd5e82-207e-39a5-9efd-b7738bb4c691 | -19.29826 | -54.64153 | 2026-03-04 05:27:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.1 |
| c39b5df2-3be7-303b-b4c6-ce4606a43eee | -16.58591 | -58.21872 | 2026-03-04 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0c932b24-287e-3e42-802e-ed46a5fb3fee | -16.58197 | -58.21809 | 2026-03-04 05:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 89732409-7a73-34eb-b139-0ca424dfb764 | -19.20536 | -54.16944 | 2026-03-04 05:27:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 3c05f814-a8dc-3e10-9c4e-0344d83143d9 | -14.2107 | -59.37304 | 2026-03-04 05:27:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b5fe1bf-224e-3b8f-ac39-ee5c36a060f8 | -18.84294 | -53.40995 | 2026-03-04 05:27:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 05034a64-a87a-375a-a573-5b6b34c44b67 | -15.42577 | -52.19704 | 2026-03-04 05:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fa2ee37-c0cd-38fa-ba14-78f7681f1f81 | -20.72953 | -51.23098 | 2026-03-04 05:27:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4cc657ff-96b6-398a-8406-46e23dd7f1bb | -16.99473 | -55.10401 | 2026-03-04 05:27:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 57422cce-c175-3f14-9667-275df7515a31 | -17.89372 | -57.20125 | 2026-03-04 05:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 7235853e-5b4f-3ddd-93e8-a77316de8d00 | -20.00399 | -51.8377 | 2026-03-04 05:27:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40d91093-6cf8-3347-b333-d8f422faf468 | -19.88884 | -54.22519 | 2026-03-04 05:27:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.1 |
| c5be0775-a190-35d3-8cf2-5b510799c153 | -17.69737 | -53.72559 | 2026-03-04 05:27:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40a8db36-d6fe-301c-a559-2a79d156c3c8 | -16.93531 | -55.78915 | 2026-03-04 05:27:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.2 |
| 3b2b853c-0991-32a3-aaff-36f796a94a5d | -20.93637 | -56.89408 | 2026-03-04 05:27:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdac22ae-6680-379c-bc3f-eb57bc5fb15f | -18.16428 | -53.44517 | 2026-03-04 05:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 927f4573-5ec2-3b2f-a569-1851ca5e2d88 | -18.59149 | -55.90182 | 2026-03-04 05:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.2 |
| d50ba350-917d-3f43-9ebd-340643ddaefd | -15.49109 | -52.55824 | 2026-03-04 05:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| e11ce7a4-af3d-3fbe-b07f-a77d037c153a | -16.46029 | -53.52095 | 2026-03-04 05:27:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d90e5d5c-8339-374f-afe4-5a82717b628d | -22.31085 | -55.31918 | 2026-03-04 05:29:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 5e3d560a-6e16-398c-9c9d-2fb419e207c5 | -21.98576 | -53.53665 | 2026-03-04 05:29:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 752670c1-7911-3753-a518-70edb058ff44 | -21.70476 | -56.32117 | 2026-03-04 05:29:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54a54405-71ba-33ef-964e-c0952c3d8293 | -22.78273 | -55.39347 | 2026-03-04 05:29:00 | NOAA-20 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0a0d746d-4bf5-32b0-bf02-8b5d17554049 | -25.21521 | -53.28736 | 2026-03-04 05:29:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 07eb9294-5275-3718-ad02-ab839ee86d32 | -24.99638 | -50.72303 | 2026-03-04 05:29:00 | NOAA-20 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 82651f71-5cc3-381e-9db5-b903f21544e2 | -24.65758 | -52.82956 | 2026-03-04 05:29:00 | NOAA-20 | CAMPINA DA LAGOA | PARANÁ | Brasil | 4103909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 0c4028b8-38a5-320e-8955-435f07274914 | -26.74114 | -50.97951 | 2026-03-04 05:29:00 | NOAA-20 | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a74c0fc3-3fe9-3459-81ef-4279482e99a6 | -22.74495 | -51.81876 | 2026-03-04 05:29:00 | NOAA-20 | SANTO INÁCIO | PARANÁ | Brasil | 4124509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| c5060bd9-4c74-3b9c-89fc-93e0b6de5664 | -25.74616 | -52.50855 | 2026-03-04 05:29:00 | NOAA-20 | CHOPINZINHO | PARANÁ | Brasil | 4105409 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| b061a3e1-eae1-3d16-9792-6b423983744c | -21.70454 | -56.3223 | 2026-03-04 05:29:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4d6b9b4-2c3f-38aa-9f86-fa6a16679d16 | -22.62427 | -54.95083 | 2026-03-04 05:29:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b62ffcb6-a724-39c4-906e-88ac6b5fc4f1 | -27.1846 | -53.00851 | 2026-03-04 05:29:00 | NOAA-20 | ALPESTRE | RIO GRANDE DO SUL | Brasil | 4300505 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c3c2d1d3-401d-3dab-9e95-7b1295ef38ed | -27.21778 | -52.68786 | 2026-03-04 05:29:00 | NOAA-20 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d901194b-f9db-355c-ad50-3ea262381b54 | 1.5047 | -59.9116 | 2026-03-04 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 9bc03c94-364f-3d8a-9224-85297ece5b5f | -30.60417 | -55.12698 | 2026-03-04 05:31:00 | NOAA-20 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| 428a370c-049c-397e-b2f7-f9d5e2ef2561 | -29.83675 | -51.44202 | 2026-03-04 05:31:00 | NOAA-20 | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| e0d60381-ec74-39b8-84fd-cbd0ad6598ad | -28.86932 | -54.02652 | 2026-03-04 05:31:00 | NOAA-20 | JÓIA | RIO GRANDE DO SUL | Brasil | 4311155 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| b1a7b80f-55ed-31f2-bb9d-99871d4a66c9 | -30.33075 | -53.25579 | 2026-03-04 05:31:00 | NOAA-20 | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 814abbc6-cdf9-355f-9f5d-a17fbec7ecc1 | -31.89553 | -52.51056 | 2026-03-04 05:31:00 | NOAA-20 | CAPÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4304663 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| eeb86242-0eaa-359a-9873-a8e4d3a49cbe | -29.65213 | -53.8196 | 2026-03-04 05:31:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 819729c3-4cd7-3eb3-ad05-b0931c4d61d9 | -29.21757 | -52.40953 | 2026-03-04 05:31:00 | NOAA-20 | PROGRESSO | RIO GRANDE DO SUL | Brasil | 4315156 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4c87d2ea-3527-3bec-9d26-833ef5e62885 | -29.79969 | -51.51472 | 2026-03-04 05:31:00 | NOAA-20 | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| c397f0ad-f4e4-3947-b9fa-fb12cbb8bdcc | -29.50525 | -56.77748 | 2026-03-04 05:31:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| aa0e9b4f-32fd-3586-8e98-33fce1912303 | -30.09515 | -50.62165 | 2026-03-04 05:31:00 | NOAA-20 | CAPIVARI DO SUL | RIO GRANDE DO SUL | Brasil | 4304671 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 66d4964c-9644-30d0-b1c9-9af81568f4f2 | -32.4977 | -53.02354 | 2026-03-04 05:31:00 | NOAA-20 | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 0f6d3dfa-f691-3adc-bb14-d4e145f7147c | -31.63594 | -53.63383 | 2026-03-04 05:31:00 | NOAA-20 | PEDRAS ALTAS | RIO GRANDE DO SUL | Brasil | 4314175 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| ca36e9da-40b4-3565-94ce-3ad43b0a372a | -30.19654 | -54.26212 | 2026-03-04 05:31:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| 96b4094a-0833-383b-ac18-9ec06333d685 | -28.69293 | -51.6706 | 2026-03-04 05:31:00 | NOAA-20 | NOVA BASSANO | RIO GRANDE DO SUL | Brasil | 4312906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 892d308f-eede-3605-b62f-bc0d85a8e4e4 | -31.20246 | -52.18565 | 2026-03-04 05:31:00 | NOAA-20 | SÃO LOURENÇO DO SUL | RIO GRANDE DO SUL | Brasil | 4318804 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| 2198a27c-0a32-35f3-b97f-e05a271cefa8 | -28.43662 | -53.09906 | 2026-03-04 05:31:00 | NOAA-20 | SALDANHA MARINHO | RIO GRANDE DO SUL | Brasil | 4316436 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 74f931b5-1229-390e-9a40-379f17d7997b | 0.0455 | -60.9988 | 2026-03-04 05:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 86.6 |
| c2fdf701-e499-3623-abbd-2158dc648167 | 0.0455 | -60.961 | 2026-03-04 05:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 46.5 |


[Clique aqui para ver as próximas entradas](README11.md)
