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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0305449-ac07-33dc-a3a0-e02f38baa1c7 | -12.53197 | -58.34096 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88a9445a-8375-35f8-b1c2-bc43f4f25aa9 | -12.55806 | -58.36712 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c3412fe1-e394-3d4d-86ac-eeb8de759920 | -12.55012 | -58.37037 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34022fee-e620-3170-8c04-e9e8a4664d3c | -13.48388 | -60.34773 | 2024-12-11 05:22:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc51dbae-0bf9-3349-bc77-35b704754078 | -13.48728 | -60.34827 | 2024-12-11 05:22:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77273e88-8717-3c1a-8ff9-4aca53d01aad | -12.57195 | -57.76273 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d7c3643-d741-3ddb-8fdf-2a6e4c97a324 | -14.57009 | -56.71312 | 2024-12-11 05:22:00 | NOAA-20 | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a33d462e-a590-3f88-85c7-40e75497318e | -9.83005 | -63.09961 | 2024-12-11 05:22:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3cc6bec-2e6f-3a16-9a51-0963277c6bec | -11.66206 | -58.26885 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d50ecfa8-d7f5-33ed-924e-3b1ab2a9d578 | -11.09614 | -54.6251 | 2024-12-11 05:22:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69710da9-7426-3d61-b4e9-dcedfce58c48 | -12.54596 | -58.34756 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ff7c5a2d-6d80-35ed-8492-753b6a3e7a8f | -12.56758 | -57.76498 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8644fda6-b331-3e33-b82a-034f94a2b08f | -12.70731 | -54.97015 | 2024-12-11 05:22:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9717cd5c-606a-3661-9888-62f78626c35b | -11.36962 | -57.79464 | 2024-12-11 05:22:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8678c9e7-876c-3db9-86aa-9980387bb467 | -12.56537 | -58.36818 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ac7813a-b77e-3c67-91fe-2bfca2b0487d | -12.56381 | -57.76443 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1b2f14b0-037e-3622-9746-2bd381601138 | -12.55138 | -58.36171 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 288390a0-12bd-3dfc-8eb1-6e1e3b1b3ffd | -12.54105 | -58.35572 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6e167c2b-d524-31d6-84a2-091aecfc3969 | -12.54356 | -58.33831 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6351a21d-85f9-3cb3-95c0-46faf0c16174 | -12.55869 | -58.36278 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 96a7d62d-f175-3848-b6ce-5c8d46a0206a | -12.53135 | -58.34529 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2a99957-5b3f-3a59-9b1f-9d96e5c7cc16 | -14.57424 | -56.71366 | 2024-12-11 05:22:00 | NOAA-20 | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7f2893a-4ff1-3aa8-8ded-10d904abc603 | -12.91657 | -55.04656 | 2024-12-11 05:22:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e18eca5-4b40-3836-b462-1c0a48ba46c8 | -10.02654 | -53.75171 | 2024-12-11 05:22:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9282eec-2744-36b0-8613-c532c3f81e7a | -11.11632 | -54.64675 | 2024-12-11 05:22:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c89c92f-aefc-3edd-b97c-6a35155bbcf7 | -12.56817 | -57.76218 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8549bb29-c832-3ae5-a15f-1ffb25e2502d | -12.54293 | -58.34266 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ae609225-deb0-3a3a-af2f-17ed5d18a914 | -12.56374 | -57.76632 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 10024a4b-c488-327a-ba68-67c5e3e5feb3 | -12.55377 | -58.3709 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 01103acb-6f9e-39d4-89b6-8a9cad2b5ce8 | -11.78134 | -55.12758 | 2024-12-11 05:22:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae5acdab-3252-3d42-8b5d-fa017cf2b04f | -12.55265 | -58.35295 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7e4dfc6b-18f4-320c-b279-ccd4eb81da19 | -12.54659 | -58.34319 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 361b6658-ed05-3221-ac69-6e4925d563ab | -12.54647 | -58.36983 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 591ce53e-0546-3c4d-972e-3bc4219d1884 | -12.55088 | -58.33934 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e09a7bd1-ff6d-364c-881d-0723b4463ba5 | -11.3659 | -57.79414 | 2024-12-11 05:22:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73bf4348-c795-31cf-b025-e5fcb475f17a | -11.11694 | -54.64216 | 2024-12-11 05:22:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c191f0b9-71f7-35b6-9c55-ead49e96a79f | -9.16207 | -62.61176 | 2024-12-11 05:22:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1444e53-d30d-3b2a-b831-ad10665d7b8b | -12.90693 | -55.04985 | 2024-12-11 05:22:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7feb4f0-d0f5-35d1-a8ec-947fbf53187b | -12.53562 | -58.34154 | 2024-12-11 05:22:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6f4dd43d-955d-3708-81bd-8191ece083d7 | -16.26804 | -59.5192 | 2024-12-11 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0121680-f7af-3ff7-94c8-50618471a6b7 | -15.96761 | -57.17044 | 2024-12-11 05:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f2e0e43-bd72-3fdd-bc06-6e538bccd8da | -17.74087 | -54.2161 | 2024-12-11 05:25:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bda63a9-6d43-3af1-a9b2-df80ab36c2ef | -17.74121 | -54.21294 | 2024-12-11 05:25:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b1692b3-b0c4-33fb-9a53-9802a11e0ccd | -15.96401 | -57.16608 | 2024-12-11 05:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2710c7e-5d51-3567-8491-54d45df31e04 | -17.74313 | -54.21526 | 2024-12-11 05:25:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da400349-85fa-345e-9e19-85803c323ede | -17.74276 | -54.21841 | 2024-12-11 05:25:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| baa4baf4-023a-3c35-9af5-8d601b201068 | -15.96811 | -57.16665 | 2024-12-11 05:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d27c062-347a-3710-b30c-77d8a79786cd | -15.97221 | -57.16723 | 2024-12-11 05:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9e19ba0-4ac1-3416-88fe-13637f2036bf | -15.9758 | -57.17159 | 2024-12-11 05:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e1b22ae-2c1a-31d8-93ad-7e7f97f9d715 | -16.08105 | -60.09115 | 2024-12-11 05:25:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b25424c9-ad21-3e41-ba94-14a4ade09ef7 | -17.74019 | -54.2224 | 2024-12-11 05:25:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e7268ad-a3e5-3c42-9f35-a4fcbb69e3a5 | -15.97631 | -57.1678 | 2024-12-11 05:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eecea7ce-f324-36bf-824e-2eb531ae8874 | -15.97171 | -57.17101 | 2024-12-11 05:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1e44c61-e04a-320b-99e1-fd3d54a1c6a1 | -17.74053 | -54.21926 | 2024-12-11 05:25:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc507c2a-4b47-32b0-bd8b-fa5611dc2e9e | -17.7424 | -54.22155 | 2024-12-11 05:25:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 582393af-fd5c-30c2-a13a-a786637c9306 | -15.96862 | -57.16287 | 2024-12-11 05:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de2b9c80-4f5a-351f-8900-e6e90546963e | -6.12429 | -42.54005 | 2024-12-11 05:29:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 235.1 |
| 2b868a74-3160-33fd-8f03-b2023b5f4be1 | -6.12234 | -42.55409 | 2024-12-11 05:29:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 8115a129-4624-3268-a603-f15ec3e47035 | -6.90918 | -43.5031 | 2024-12-11 05:29:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 512a6367-00d4-3cdf-b630-197a98319621 | -5.98214 | -44.59978 | 2024-12-11 05:29:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7e3b9221-5658-37b9-9ffa-c4257ccd088c | -6.97037 | -42.98535 | 2024-12-11 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| ba936517-bf89-3eef-ba64-fed25246f406 | -6.95196 | -43.00462 | 2024-12-11 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| e53dcb2e-4def-37e6-97f1-ea922362ebe8 | -6.94703 | -42.99569 | 2024-12-11 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| b6589d7d-004f-3158-922a-eaa0231896dd | -6.91092 | -43.49069 | 2024-12-11 05:29:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 73593e9f-07dd-39f5-bf61-9d77d38d0416 | -6.94314 | -42.98969 | 2024-12-11 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| ff0837ca-1bb9-3ac6-9ff6-7ca098d86438 | -6.96852 | -42.9988 | 2024-12-11 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| a516d28f-b219-3b84-a484-ade4a121a5d4 | -6.12626 | -42.52593 | 2024-12-11 05:29:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 63.3 |
| fdad8475-a9f7-3a2e-8ab8-cc6e07811905 | -11.11926 | -54.62844 | 2024-12-11 05:29:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| f348203f-0733-337e-852f-59a70afea963 | -6.97927 | -43.00034 | 2024-12-11 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 8d2355de-5cbd-38db-a4e1-13e0190f6442 | -6.95778 | -42.99722 | 2024-12-11 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| e69c65bc-ddbe-343d-a78f-2f683b271f09 | -6.90745 | -43.51543 | 2024-12-11 05:29:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6a41817d-cb0d-34a3-9bd3-39d7fd6cc437 | -6.89712 | -43.51398 | 2024-12-11 05:29:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 32f037bb-dd20-3e61-9766-4706a1543c44 | -6.11525 | -42.52442 | 2024-12-11 05:29:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 9a5e5987-1788-3e9b-9fca-7159dde10091 | -6.89884 | -43.50165 | 2024-12-11 05:29:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| cd41805a-09f3-30fa-bc27-e0a6ce46fe56 | -6.95389 | -42.99121 | 2024-12-11 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 42.7 |
| f1803347-134d-3a69-9099-0553623a0c5d | -11.10654 | -54.62609 | 2024-12-11 05:29:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 92758467-19b8-3324-905a-e93990d31454 | -11.11585 | -54.64833 | 2024-12-11 05:29:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 1a423b3e-a2fc-3131-a105-cc2241f2fd6e | -6.09626 | -44.04464 | 2024-12-11 05:29:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| dcb7019b-28b4-3d20-bdae-abc0c49a56f0 | -12.67026 | -45.66486 | 2024-12-11 05:29:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 496fd1c4-7260-3412-892b-a597cd5db2c5 | -6.98114 | -42.98686 | 2024-12-11 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| b35f0210-86ab-39d5-834f-ee0b15e3b00b | -6.95962 | -42.98375 | 2024-12-11 05:29:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 44dc3b02-821b-3b2d-ab3c-25538ad45314 | -6.1368 | -42.5307 | 2024-12-11 05:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 139.2 |
| c01afab9-72bc-365d-b569-40e9f93b7f46 | -6.897 | -43.5202 | 2024-12-11 05:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| be63db12-a105-33d9-9a02-c28b0ae3b13e | -15.0867 | -59.6288 | 2024-12-11 05:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| b270608b-e0b8-3960-a416-745d640f96b5 | -6.9158 | -43.5185 | 2024-12-11 05:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| d581ec1f-a6dc-3ce0-b8f7-a241a3715f97 | -6.9161 | -43.4952 | 2024-12-11 05:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 7fbcf321-a146-3115-b0a4-5cce29d098c8 | -6.118 | -42.5323 | 2024-12-11 05:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| e1442cbb-1074-3805-a57d-4f0173f8fb6f | -6.9592 | -42.9994 | 2024-12-11 05:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 139.7 |
| 0119ece3-5276-380c-a3f8-ebb876182b25 | -15.0865 | -59.6487 | 2024-12-11 05:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 6a50f6f7-a2ff-3346-a761-f587ee796769 | -6.8972 | -43.4969 | 2024-12-11 05:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| f80c38d9-8114-34ae-b019-5d73bc9ee1cf | -6.978 | -42.9977 | 2024-12-11 05:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.2 |
| 8c01fff4-2dff-30bc-9f27-31ff0bdab1e9 | -6.1366 | -42.5544 | 2024-12-11 05:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 5e4866b4-6892-3c54-bd90-d7f2a29fff32 | -6.1178 | -42.5559 | 2024-12-11 05:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 2f3bbe50-71f2-35ed-b775-5e48c3ee3b97 | 2.7627 | -60.6378 | 2024-12-11 05:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 1d629b62-5d27-3fe2-9ec6-8bbeda512198 | -14.96914 | -44.40821 | 2024-12-11 05:31:00 | AQUA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 183b3f06-10e6-397d-ade2-ab9d7e2e86bf | -12.70897 | -54.96403 | 2024-12-11 05:31:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 70a1dfb7-029e-346d-a9da-15ecefe5c14d | -12.5427 | -58.3362 | 2024-12-11 05:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| ab021888-4063-3f3a-88b7-1ef3b4512316 | -12.5615 | -58.3546 | 2024-12-11 05:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 1eba48ed-97b8-3ca7-b11b-3dd6e179fe71 | -6.897 | -43.5202 | 2024-12-11 05:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| c6e47ed0-805f-35a7-992b-bd804069d052 | -6.9158 | -43.5185 | 2024-12-11 05:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |


[Clique aqui para ver as próximas entradas](README29.md)
