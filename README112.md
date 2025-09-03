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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81b3ae16-25b7-3cb4-9dce-b9120b305c85 | -8.8839 | -45.8446 | 2025-09-03 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| e2727c9a-ea08-31e3-9afd-6548e7817800 | -6.7595 | -45.9095 | 2025-09-03 12:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| b6438a53-4096-3d13-be70-7a10051ecd39 | -10.0932 | -54.7667 | 2025-09-03 12:20:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 422fb89c-1a36-3dea-b730-d11b70c1a36a | -6.2411 | -43.3677 | 2025-09-03 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| d2c4a1bd-1c07-3ef4-b342-cfb242c19ede | -5.8109 | -43.239 | 2025-09-03 12:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 2fb109f1-b87e-374a-a32a-cd2fc72dec3b | -8.0794 | -45.3844 | 2025-09-03 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 5e4889d4-33ab-3311-96d6-a556ae4dd483 | -8.0608 | -45.3636 | 2025-09-03 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 97a48931-6039-3f0a-9707-21397ea9b34b | -8.8842 | -45.822 | 2025-09-03 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 90d5127c-c140-3baa-9e29-2b7162ad4720 | -10.4853 | -50.346 | 2025-09-03 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| b3635dbe-be51-381c-85ad-b64dee6a07b0 | -8.0197 | -44.1072 | 2025-09-03 12:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 7c572ecd-cc89-3ac5-85d9-610568edec77 | -7.4842 | -44.8043 | 2025-09-03 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| dff33d9a-7bbe-3efe-99ef-708b5af2d97e | -11.6165 | -52.0689 | 2025-09-03 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| acc16668-ccb5-3e54-aff4-9de927a73a75 | -8.7969 | -49.8679 | 2025-09-03 12:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| a93726ce-d220-36c9-bc57-5c1485ad5043 | -6.2224 | -43.3693 | 2025-09-03 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 274.3 |
| b99484b3-34f9-31d9-8575-3b5fda8de341 | -10.5045 | -50.3226 | 2025-09-03 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 309b9c4d-459c-3261-85c4-e0efdef168eb | -10.4856 | -50.3246 | 2025-09-03 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 69b06240-6c80-31fa-98e8-7e5e6085b8a9 | -16.8532 | -49.6196 | 2025-09-03 12:20:00 | GOES-19 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 5c095102-048b-3d87-bca0-dc3d9f22f549 | -6.2036 | -43.3709 | 2025-09-03 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 750b8b2c-6759-3a59-8bc3-dab99bfeb767 | -7.5302 | -47.4443 | 2025-09-03 12:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 362591b2-0147-39f1-85e8-5ca4c8850708 | -9.6232 | -47.0416 | 2025-09-03 12:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 5dfa6e51-09a5-33a7-8720-3c702cc8bace | -6.2409 | -43.3911 | 2025-09-03 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 66a79b8f-5293-39af-8492-9b7d36aee174 | -9.7427 | -49.414 | 2025-09-03 12:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 41582ca6-bcfa-331f-a15e-1f2d512c1161 | -5.8111 | -43.2156 | 2025-09-03 12:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| e958c636-08d7-36c0-8615-b3c492839a3f | -8.0796 | -45.3617 | 2025-09-03 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 0f8a4f82-5590-3593-9c12-971f7688c57d | -6.2221 | -43.3927 | 2025-09-03 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 241.4 |
| 14e4af0d-5ca5-3f17-851b-c3f7865efb55 | -15.2675 | -52.7261 | 2025-09-03 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 40b225a0-a760-3979-b160-046e4da7ea43 | -5.8455 | -45.6421 | 2025-09-03 12:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| a78427fb-cd03-30a7-96c6-3490a0b8c02e | -8.8653 | -45.824 | 2025-09-03 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| e75479c3-920c-3034-97f0-1a3d935851a1 | -6.7595 | -45.9095 | 2025-09-03 12:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 5ca19c35-cd00-35fc-9422-64b36cb18457 | -6.204 | -43.3241 | 2025-09-03 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 71007126-8af2-32b0-9b45-7dd66f75bcf3 | -10.4853 | -50.346 | 2025-09-03 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 477d0363-a26d-3545-be9b-b320b3da732c | -11.8537 | -51.4106 | 2025-09-03 12:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0da3250f-b6ce-3ef6-8822-303d0661c90e | -15.1771 | -52.356 | 2025-09-03 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 52a81b73-f04a-3d3d-aef2-081dc3377faf | -7.53 | -47.4662 | 2025-09-03 12:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 1fe3c8a0-7faa-3ee8-af21-4dac6b51cbcc | -11.9606 | -50.6108 | 2025-09-03 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 41ccfcca-597f-3a17-892d-e12e038d0ac3 | -12.7926 | -47.6638 | 2025-09-03 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| ac05cafa-08c8-3426-b251-2bc52a86db12 | -12.793 | -47.6415 | 2025-09-03 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| dc830544-d020-3d73-971d-b52ecd867e57 | -8.0608 | -45.3636 | 2025-09-03 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 1cac1a9b-0cf2-38a3-80bd-fa893aa25b08 | -9.96 | -51.6244 | 2025-09-03 12:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 799bccf7-b50d-3de2-830a-fc098de42686 | -6.3689 | -45.6483 | 2025-09-03 12:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d7eff303-5011-386f-94e5-78fdfbc777cf | -12.4071 | -47.7849 | 2025-09-03 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 28b9cd09-5c1e-3107-9f60-0e0b1f1328e4 | -11.6165 | -52.0689 | 2025-09-03 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 487cf4dc-ae18-332b-9df2-a844e053b1ef | -7.4842 | -44.8043 | 2025-09-03 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| daa7eddc-2771-3139-9783-bfd39969c7ef | -9.7427 | -49.414 | 2025-09-03 12:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 887320c7-544a-3bde-997e-8676bbdf6b31 | -11.8533 | -51.4318 | 2025-09-03 12:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 0a4904c2-6c6a-385f-adf2-c99db2a4b79e | -8.0796 | -45.3617 | 2025-09-03 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| c2c6476a-07eb-3b2a-aedc-c8f488e33581 | -7.5302 | -47.4443 | 2025-09-03 12:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| de133417-e1b2-3549-b0e7-e4f4d36e6463 | -9.6232 | -47.0416 | 2025-09-03 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| dc716165-9b69-3e8b-8b6b-1f7815c667f4 | -9.6418 | -47.0618 | 2025-09-03 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c93de232-fbbd-3cf2-869d-528c7a019ff1 | -10.9323 | -50.8529 | 2025-09-03 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| e55826e7-6f6b-3d40-aaf8-46ea2a4d976c | -6.35 | -45.6723 | 2025-09-03 12:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 7fec6c49-6432-35b1-8776-995c4faa22f5 | -6.797 | -44.0859 | 2025-09-03 12:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 1d7607f6-a0e7-3fa5-b739-1098d4fde7ef | -15.2675 | -52.7261 | 2025-09-03 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| f074f475-3a5b-378c-85d2-8ba540249962 | -10.5045 | -50.3226 | 2025-09-03 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 34e308c9-dd1e-3446-bc46-523cc53ab508 | -9.6229 | -47.0638 | 2025-09-03 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 323.6 |
| 866d75dd-b137-3694-989f-577e4e2082fb | -6.3502 | -45.6498 | 2025-09-03 12:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 4d98edfb-16c4-3a48-b3ed-34ae9c1e05ba | -10.0932 | -54.7667 | 2025-09-03 12:30:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 115.7 |
| afc6141f-e18b-3baa-8e9c-5229604eb915 | -11.8533 | -51.4318 | 2025-09-03 12:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 87afdcab-d4f2-302e-ac01-3b27c22ed815 | -11.6836 | -57.3518 | 2025-09-03 12:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 418e4861-1403-39e2-8fb4-24daf52e2dea | -7.4842 | -44.8043 | 2025-09-03 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 88c1cb2b-7936-309a-9a6e-3ad2c56cc1b5 | -9.96 | -51.6244 | 2025-09-03 12:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| fcd81ea4-c1e7-35fc-b072-fa9a1e60ec54 | -9.631 | -47.8589 | 2025-09-03 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| c9648998-1911-3dc3-95ba-7383f7aa97de | -8.3644 | -48.3116 | 2025-09-03 12:40:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 6f86cc11-a812-3c5a-a892-3d909481ae70 | -5.8109 | -43.239 | 2025-09-03 12:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 8ddc2798-a7f2-3cb6-afd2-55377edf5b53 | -7.484 | -44.8272 | 2025-09-03 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| aeb7bf99-7460-35a9-8c8c-403c3f864d0b | -10.9136 | -50.8336 | 2025-09-03 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 8c34a691-9014-3888-b60b-1dd10dbad257 | -10.9133 | -50.8549 | 2025-09-03 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 5e670b1d-d039-3ea7-a8e2-900eccf9cd2a | -8.0796 | -45.3617 | 2025-09-03 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 60145e26-9a7b-3f2e-ac40-388bfd499a92 | -7.7039 | -48.7371 | 2025-09-03 12:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 9abd7234-d02f-3d61-b0f6-df0412a6183b | -15.2675 | -52.7261 | 2025-09-03 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 4cc20c75-d9a9-33fa-bc43-9dc65d385872 | -5.8455 | -45.6421 | 2025-09-03 12:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 305.5 |
| a7dcac91-ec31-39c4-9d9b-fbbcda5bc5cd | -8.0608 | -45.3636 | 2025-09-03 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 222.9 |
| c17ec8d5-293d-33de-b8e2-59fa0bc627b6 | -9.7613 | -49.4337 | 2025-09-03 12:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 45e84e9a-f554-391a-8185-3ad1a2eacc92 | -7.0128 | -43.2525 | 2025-09-03 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 49eed5db-d503-36e9-8bb1-bfee08366b07 | -6.4648 | -49.5151 | 2025-09-03 12:40:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 701f9799-6c35-38b1-9442-4c1ba2e24a94 | -6.4646 | -49.5364 | 2025-09-03 12:40:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ee5dd810-cd8d-3e91-b91d-60be139f660c | -7.5302 | -47.4443 | 2025-09-03 12:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| b63e1d54-55d1-3902-a4ce-8f6aa7c84351 | -8.8653 | -45.824 | 2025-09-03 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 85eb5f62-92ce-3f38-a67e-fc5e3cae1573 | -8.0794 | -45.3844 | 2025-09-03 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 77d0d96b-66ff-35f4-8b4a-6c3329d94b16 | -7.7226 | -48.7355 | 2025-09-03 12:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 55ba25fa-6fc8-3781-9a8a-d78b78bdd4a1 | -10.9323 | -50.8529 | 2025-09-03 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 58299428-9a9c-3ee6-b416-0207f01d5e61 | -6.0784 | -44.6961 | 2025-09-03 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 3c0c1926-66c9-3f62-8c64-1796c8ad6ca7 | -11.6647 | -57.3533 | 2025-09-03 12:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| beb2da7e-fcab-324e-aaca-2f4d19f0c005 | -9.7615 | -49.4121 | 2025-09-03 12:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| a61b6355-9a4b-3030-9f4e-784caafccf7f | -5.8642 | -45.6408 | 2025-09-03 12:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 211.7 |
| ae13fcff-391b-35e8-b930-edf5b7c88ea7 | -7.53 | -47.4662 | 2025-09-03 12:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b38d4837-3099-374e-a885-ca17e8705b6f | -12.7926 | -47.6638 | 2025-09-03 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 29093d49-ef6a-30bb-955a-fdd8c8a5be7a | -10.9326 | -50.8316 | 2025-09-03 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| a1ea287e-2b1c-3c86-8117-be1c2440e27f | -6.7967 | -44.1091 | 2025-09-03 12:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| e6c77e52-6f07-36b6-969c-6d66a64a25e0 | -10.0932 | -54.7667 | 2025-09-03 12:40:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 7355aede-b0f9-3fec-8783-40d4ad2d2b7c | -9.6229 | -47.0638 | 2025-09-03 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 1f7859e5-a694-3c56-91cf-8430b34feeb7 | -7.7036 | -48.7587 | 2025-09-03 12:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 171.8 |
| 0f8d89ea-49b4-3135-b2d9-f4394c0df0a5 | -6.797 | -44.0859 | 2025-09-03 12:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 803fd33b-e4bb-361f-b514-58305e7aa5df | -11.9635 | -45.7741 | 2025-09-03 12:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9f9e55fd-6ce5-32bf-bf3e-894dd2ea0eb0 | -8.0197 | -44.1072 | 2025-09-03 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a5f283bb-30bc-3a55-b063-d84ad183167d | -9.402 | -48.0585 | 2025-09-03 12:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 3c4befcd-fee6-3053-954b-f54c604d057f | -9.7427 | -49.414 | 2025-09-03 12:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 42835845-c940-3714-906e-d7d1fddbe56b | -5.8111 | -43.2156 | 2025-09-03 12:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 07d8a01a-cdc2-39e8-a3e8-5741347c88a3 | -10.9524 | -50.7658 | 2025-09-03 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 5331537c-6d6e-33c0-9d56-5a757583e2b5 | -7.0131 | -43.2291 | 2025-09-03 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |


[Clique aqui para ver as próximas entradas](README113.md)
