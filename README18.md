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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b594f85-c12f-3bf1-acf8-f4a3474e3423 | -10.41775 | -50.73402 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 30.3 |
| bbf9392a-1e56-3597-b746-5ce51830e11b | -10.425 | -50.70567 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| fd2438ad-6b0f-3069-a3e1-30d3cab1cf8f | -10.41602 | -50.72055 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| b2ab20a1-c08e-3eb0-8f37-73f0a9415ce6 | -10.12988 | -48.83304 | 2024-10-06 00:52:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 10d84ede-8c1a-30d7-8bbf-165fa7db4ffb | -10.12855 | -48.82295 | 2024-10-06 00:52:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2a68c49d-f02f-3752-8487-b83c63b7f11d | -10.12844 | -48.32721 | 2024-10-06 00:52:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5cfb5e98-3db1-3f68-816c-be0dc7f8b3f8 | -9.24564 | -43.51365 | 2024-10-06 00:52:00 | TERRA_M-M | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 8737fbf0-7f7f-3d87-9801-6b79b3935132 | -9.1918 | -45.56337 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 492d7b8b-6ff8-3b0d-b686-e38213c5bc5a | -8.18129 | -43.72593 | 2024-10-06 00:52:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| a136a67a-a077-3e0e-9c05-25fb241b8df6 | -8.14949 | -44.41341 | 2024-10-06 00:52:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c3542981-82a3-3ed6-a968-396f8d5d898e | -8.10853 | -43.78989 | 2024-10-06 00:52:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 91e897e9-a166-382b-99f9-1cdef8a908a1 | -8.10821 | -43.78361 | 2024-10-06 00:52:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 07c3f0db-71f2-3888-97d3-a9c5d76ea13d | -7.76804 | -43.08508 | 2024-10-06 00:52:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| e9ff649b-5f08-306c-a527-769da038e326 | -7.76613 | -43.07236 | 2024-10-06 00:52:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| c59c2489-1c30-3087-a8ae-88832881e267 | -7.74313 | -43.06288 | 2024-10-06 00:52:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ad6ebd57-16b6-3c2e-acad-fbae05c7a38e | -7.74117 | -43.04999 | 2024-10-06 00:52:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 85812134-f8a1-33ca-8d2d-f690f5d05aa7 | -7.73255 | -43.06431 | 2024-10-06 00:52:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| efac6966-8326-37cb-94b0-924e41e028c3 | -7.69329 | -42.98282 | 2024-10-06 00:52:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |
| d36c10e7-59ba-3378-828a-941a7613eb6b | -7.69133 | -42.96961 | 2024-10-06 00:52:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 2de607df-5397-3e82-ac11-653ca9a4f1c3 | -7.63368 | -42.49451 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 6238e355-688c-3f78-abce-c0dedc276d65 | -7.63298 | -42.50032 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 7e1f58cd-ad33-34a7-ae6b-b0c7160dc2a4 | -7.4651 | -44.77719 | 2024-10-06 00:52:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f9f2cffd-0b07-34df-b0c8-f8ec0209b44b | -7.46361 | -44.76694 | 2024-10-06 00:52:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b31d1756-2df5-38ce-8e76-b904012b68cc | -7.13457 | -42.62329 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| c1ef334a-d737-300b-8248-65b60bbdba9f | -7.12355 | -42.62501 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| d8b87b9f-6b99-3a17-94ac-a6b4cc7cf795 | -6.828 | -42.81038 | 2024-10-06 00:52:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 70799d27-cc3d-37d8-b222-5d79de48ee4b | -6.07821 | -42.33659 | 2024-10-06 00:52:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 159598da-8aa3-3e88-a3ff-cbe0251aab52 | -14.5109 | -49.27541 | 2024-10-06 00:52:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 8a31b5cb-2c83-36dc-9c32-0f1b21cc9ec5 | -14.50943 | -49.26353 | 2024-10-06 00:52:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d8ff34a1-1c53-3a40-ad8f-19e76febd0df | -14.48149 | -49.27291 | 2024-10-06 00:52:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| aecd61cb-ac26-31e6-ba64-d7a46da087c5 | -14.48015 | -49.27979 | 2024-10-06 00:52:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| daf04e0d-0c2c-3a6a-ae84-bb34b91b8f8f | -14.47865 | -49.26752 | 2024-10-06 00:52:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 29f181af-8472-3d30-b323-4c2dcd9629df | -14.47123 | -49.2742 | 2024-10-06 00:52:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 866fde5c-3b1b-3055-9ab3-59ec4d210c0a | -14.45943 | -49.2634 | 2024-10-06 00:52:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8c2a909e-0177-3b2a-ab8a-072c866e9a01 | -13.8927 | -44.59423 | 2024-10-06 00:52:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 064cbcae-64f6-3501-8f13-f41d30090649 | -13.58972 | -48.14492 | 2024-10-06 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1f510d94-32d5-3517-ae57-2ad3e7df77fc | -13.58834 | -48.13446 | 2024-10-06 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0a2675cf-4149-33d9-a652-145358af2b19 | -13.52174 | -48.62708 | 2024-10-06 00:52:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d19dd4a9-2c43-34ff-8ec6-b56a4eed5132 | -13.5135 | -48.63979 | 2024-10-06 00:52:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8cc39cbf-71be-3b43-a33f-be0f95168040 | -13.51204 | -48.62841 | 2024-10-06 00:52:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| bb2caa9a-a6fe-305e-beb2-1bcf6095ce31 | -13.10516 | -46.39081 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 94358d4b-46f1-3908-bb9f-986f765310e5 | -13.10018 | -46.35452 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d170c78c-f3ff-3cdd-898d-39033541d6cd | -13.09892 | -46.3454 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 7baa5086-7f9c-3511-b795-00408520687e | -13.09863 | -44.71395 | 2024-10-06 00:52:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c09a09e0-5ac6-3c80-adeb-c15b0246cd35 | -13.09728 | -44.70451 | 2024-10-06 00:52:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7f9de39b-913f-3c56-a761-cec319f45204 | -13.0963 | -46.39211 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ee6a27a1-a937-3035-bf62-2f65c5b11c20 | -13.09505 | -46.38305 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cd5ee222-ab1b-3286-8566-7cef2f15fe6f | -13.09381 | -46.37398 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2843e76a-b7ec-304d-8533-979dd42f7f10 | -13.05113 | -40.52511 | 2024-10-06 00:52:00 | TERRA_M-M | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 62.3 |
| e182ce85-53f0-3d1d-81a4-0b4410d136a2 | -13.04931 | -40.53672 | 2024-10-06 00:52:00 | TERRA_M-M | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 21a46411-d92f-39e2-bd37-03f9b4739138 | -13.0466 | -40.52035 | 2024-10-06 00:52:00 | TERRA_M-M | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 52.0 |
| 1704167e-e6bb-394b-b294-3eb590e243e5 | -12.72137 | -40.22789 | 2024-10-06 00:52:00 | TERRA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| a9ef3431-158d-32fe-b020-ebdf899b0c62 | -12.71843 | -40.21024 | 2024-10-06 00:52:00 | TERRA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 29.1 |
| a9e6957c-3a43-3239-b3a4-ca491cabeb42 | -12.71395 | -40.21766 | 2024-10-06 00:52:00 | TERRA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 2eb1f84f-3dde-35e8-9e5e-e5209fe0af60 | -12.70638 | -40.21221 | 2024-10-06 00:52:00 | TERRA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 56158ed7-4597-3f4b-9f11-29c1571f9565 | -12.51116 | -45.30955 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fe5696a1-355b-39fb-91f2-d8b14d0b084b | -12.50986 | -45.30042 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 0691e5ce-27ad-389f-9e7e-2252cc8f313a | -12.50856 | -45.29129 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| aa7cc43a-bc9f-3d23-89b5-d6e8fb7ee8f8 | -12.50096 | -45.30177 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ed77c282-bf66-3940-9eee-9263775147c3 | -12.25545 | -41.11001 | 2024-10-06 00:52:00 | TERRA_M-M | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 7535cfc5-ce8b-30ee-a22c-5c0bbb8c8908 | -12.25302 | -41.09478 | 2024-10-06 00:52:00 | TERRA_M-M | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 37.1 |
| 13cfe318-4e62-3b97-b753-1df4aec15912 | -11.99341 | -41.34536 | 2024-10-06 00:52:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| d72c938e-e674-35cc-b924-a69659d6ac47 | -11.72293 | -44.51419 | 2024-10-06 00:52:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1b88e74a-d8cc-31e5-a9bd-3c915833e44e | -11.7215 | -44.5045 | 2024-10-06 00:52:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 0ddfd23e-0f37-306e-966c-37b57711a509 | -11.67274 | -45.2472 | 2024-10-06 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a323c81d-b0e4-38b0-9b64-addb2222be0b | -10.84652 | -42.85385 | 2024-10-06 00:52:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 33977b8a-a587-3d29-8634-d03b0c65d054 | -10.83634 | -42.85546 | 2024-10-06 00:52:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 009829e9-90be-3a66-a576-f83226eaa2e4 | -10.81282 | -44.78074 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 4c2982a4-a0aa-3d00-9922-6bf197437510 | -10.81143 | -44.77112 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 29d564cd-16d0-3d5a-a1ad-3dc76713e580 | -10.8023 | -44.77254 | 2024-10-06 00:52:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 89aa6cf6-e287-3546-ba25-4a0248ea04db | -10.48344 | -45.18383 | 2024-10-06 00:52:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 1fefc7bb-eab7-3433-8ba5-d802940d4811 | -10.23252 | -42.39178 | 2024-10-06 00:52:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| b199c80e-63e9-389e-b0eb-c1c19da3c0a9 | -10.14502 | -45.20182 | 2024-10-06 00:52:00 | TERRA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a56b5396-6e08-3564-aaad-26f4318074f0 | -9.82493 | -46.71266 | 2024-10-06 00:52:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0b74017d-6e30-3b98-9f4c-6e06b72f9a3c | -9.79085 | -50.06813 | 2024-10-06 00:52:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 22699081-eed5-3aa5-9088-c44304887f81 | -9.74318 | -50.64988 | 2024-10-06 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 83380e76-8efa-3ee6-9723-5138d6259b99 | -9.73261 | -50.65123 | 2024-10-06 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 31645074-e0f0-3227-aa57-840443dd3fca | -9.6837 | -47.83529 | 2024-10-06 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| db292475-6f24-3e17-b065-b277909b547a | -9.56643 | -50.23259 | 2024-10-06 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f6f29bff-4aa1-31d5-be3d-7aa937ae3a7e | -9.45544 | -47.58073 | 2024-10-06 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 44322846-3227-3f07-84b1-34b8e94d3a75 | -9.37498 | -51.09557 | 2024-10-06 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 8e69eff5-90f3-32cb-b7a0-a5b0782b99dd | -9.37318 | -51.08178 | 2024-10-06 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3b7fd638-1b99-3f35-8773-ab1a6b063f8d | -9.36233 | -51.08324 | 2024-10-06 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 73ae0d3d-7f2d-3bd3-961a-0f28e1b310ef | -9.35029 | -46.54863 | 2024-10-06 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 800cf1f3-0ab7-34ce-b496-9b51d33873cf | -9.3427 | -46.55883 | 2024-10-06 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 142a3a1a-c84a-3642-9405-fdc72200e608 | -9.34145 | -46.54992 | 2024-10-06 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 268.7 |
| cc8449cf-6428-3fbc-aefe-87f6a16aa96f | -9.34021 | -46.54102 | 2024-10-06 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 203.7 |
| 6cae01ba-2522-3bd2-8b77-c11efcb43afd | -9.33154 | -46.55734 | 2024-10-06 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 55f1ff60-dcdd-37ca-8813-5f457dd49833 | -9.3303 | -46.54844 | 2024-10-06 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3fe9d103-9ad2-3afe-b956-76ed89f66d94 | -9.32905 | -46.53952 | 2024-10-06 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6a4022a2-38f6-3638-8506-f01f34607ff0 | -9.28501 | -48.15338 | 2024-10-06 00:52:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 09134173-6539-3155-8595-e3fdbe42095b | -9.27711 | -48.16079 | 2024-10-06 00:52:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9590bcd5-341e-3882-b5c1-d2a005890cef | -9.27582 | -48.15137 | 2024-10-06 00:52:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f9411bcf-8d1a-3a42-a4ee-5418be6e2287 | -9.27453 | -48.14201 | 2024-10-06 00:52:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 687c27c3-c98f-381d-9ecb-3d2eca3723f1 | -9.26548 | -48.14332 | 2024-10-06 00:52:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 45c1a86f-c648-3b3b-a190-339c0fc04db1 | -9.21889 | -48.14034 | 2024-10-06 00:52:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e89cb2d5-8985-3007-911d-993a94661290 | -9.03158 | -46.58302 | 2024-10-06 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 96342a0d-48bc-34d8-98d5-a89ff5dd46d1 | -8.94111 | -49.74765 | 2024-10-06 00:52:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c401f228-f1e5-3d01-beff-b246983ec173 | -8.79495 | -49.94407 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7336cdfa-f504-38f2-8324-a2d510a7aad6 | -8.66452 | -49.42393 | 2024-10-06 00:52:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |


[Clique aqui para ver as próximas entradas](README19.md)
