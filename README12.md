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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c2b7ae5-d546-3695-ad1a-94a6059fd6dc | -3.52589 | -53.53473 | 2024-12-09 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fdb559d-24d6-3de9-9606-3bd1452008a9 | -5.57892 | -45.20797 | 2024-12-09 05:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e116bfc9-165d-3d11-8698-307bce53f640 | -4.2827 | -55.73856 | 2024-12-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7584fe1d-8a62-33a3-bcb7-697f7299ae63 | -5.8628 | -45.36294 | 2024-12-09 05:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 49c22044-774a-3687-bb64-500eac8ff17b | -6.71182 | -55.40859 | 2024-12-09 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a88f9118-ff72-3f11-9f29-6077911e1a1d | -6.23613 | -55.63045 | 2024-12-09 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7dd3154-0b8d-3211-a250-7e5b69575504 | -8.1522 | -49.14362 | 2024-12-09 05:12:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 541fd5c7-e3d2-3c5c-929b-4812ea7c18c6 | -5.57821 | -45.21342 | 2024-12-09 05:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2ca26906-4bcd-3bd2-86d0-8cbe1d1e1450 | -5.57825 | -45.21402 | 2024-12-09 05:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4bf604e1-fe76-3e3f-aaa3-02aaeace469f | -5.579 | -45.20858 | 2024-12-09 05:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5418b733-748d-369d-8271-5077f86e0430 | -8.01163 | -45.79971 | 2024-12-09 05:12:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b8f717b-befb-3628-b23a-2b9068295dd1 | -3.57708 | -53.27645 | 2024-12-09 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d9ff885-7222-35d3-b43a-6d1eab854fad | -8.01228 | -45.79456 | 2024-12-09 05:12:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9422e26-3b13-3295-893a-de0d248100b5 | -9.51904 | -54.73636 | 2024-12-09 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a53d9a7-4444-3a15-a0dd-7b7c28b0e5a4 | -7.98362 | -50.69006 | 2024-12-09 05:12:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 258ebea2-adfb-3ca8-abd2-d2fc9bfa587e | -5.57395 | -49.41529 | 2024-12-09 05:12:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03ec0b6c-53b3-363e-8544-fd5eeeda7014 | -3.57868 | -53.2798 | 2024-12-09 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eecc6522-3387-3b92-aaa1-6839fb42bdfb | -5.94894 | -44.46677 | 2024-12-09 05:12:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 54094682-f20f-3ead-ad70-274c36bf9f23 | -3.8259 | -52.33694 | 2024-12-09 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9222f162-8d8e-370c-8ec2-40bbc3656fd8 | -13.02642 | -57.22065 | 2024-12-09 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 579e3805-16c6-3bbc-8550-4296a029b0bc | -15.08887 | -59.62785 | 2024-12-09 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b40edb5-cfa5-3eea-b5f1-24da403bcfbc | -9.73455 | -61.91171 | 2024-12-09 05:14:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b659b498-7c61-3dc7-b0ab-227eb01f4398 | -10.91558 | -48.93473 | 2024-12-09 05:14:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2010e19-5169-3952-9fe4-16e6129d9b4b | -11.88206 | -54.6868 | 2024-12-09 05:14:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4702a5d-73ca-385f-906d-ad347acec82e | -12.52947 | -57.77541 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 481665ae-cafd-3a39-949d-1320d9d2ad8b | -11.65858 | -62.46569 | 2024-12-09 05:14:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2356b94-e941-3df9-8435-b737ad060481 | -10.21207 | -52.68025 | 2024-12-09 05:14:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 418dcf9d-16f5-3527-87fe-eab9454ff071 | -12.85828 | -58.22507 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51fdb488-7d49-3c76-9bda-220ca367b2b6 | -12.53497 | -57.73912 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4b90efd1-b107-3f30-b14f-313947a76bc5 | -12.79122 | -54.22267 | 2024-12-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3df2ceb8-212d-380b-97e4-366c8aaec12f | -15.97658 | -57.17454 | 2024-12-09 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4cf90637-9b5f-33ff-a955-4b2c7dd5415d | -15.98067 | -57.17102 | 2024-12-09 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 31735f9f-7adf-383e-ad6d-3d8e637d03f3 | -12.54504 | -57.74067 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d125837-aadd-3707-95fb-0227ccbe2d7f | -15.08832 | -59.63141 | 2024-12-09 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3ae1bcd-1d1e-3bed-b69b-f3d909ece436 | -12.53552 | -57.73549 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 44ce6873-71a9-3a1f-8c5a-e5892e42801a | -11.87959 | -54.67673 | 2024-12-09 05:14:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18895fdf-65f5-38a9-a5ab-f5016274ba0e | -12.53888 | -57.736 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fa79317a-8217-32ed-9cea-322bab5e1bbb | -15.08943 | -59.62429 | 2024-12-09 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05a73e33-c998-3077-b7ee-eb66d97eaa96 | -11.20612 | -53.81885 | 2024-12-09 05:14:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89664a78-1f8d-3bf5-a416-59b34d866b48 | -11.75331 | -54.72357 | 2024-12-09 05:14:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ae3fc52-39f6-3b0d-ab7b-15706315f09c | -10.92109 | -48.93551 | 2024-12-09 05:14:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 51ffdcc8-f406-3863-b22a-039a334229fb | -15.98419 | -57.17157 | 2024-12-09 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 119e32c2-1575-3dd2-8cd4-578bfdf82e26 | -12.85386 | -58.23167 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0f30dd7-1c56-3880-8fd4-144719a7e06a | -10.42699 | -51.82393 | 2024-12-09 05:14:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76eba1d0-7e56-3eee-a12d-ca28f6a83d69 | -11.05356 | -54.83752 | 2024-12-09 05:14:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebf74bd5-cb1b-375c-8932-a9ae1853a16f | -12.79051 | -54.22786 | 2024-12-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52bafd63-5e51-300a-ace1-eee3bc40bc33 | -10.83739 | -56.63179 | 2024-12-09 05:14:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0661be9c-8a5f-3405-8d2d-7a46e96d3399 | -10.83453 | -56.62748 | 2024-12-09 05:14:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 848fd2d9-812d-32be-94fe-29a8fedfa3b6 | -15.98009 | -57.17509 | 2024-12-09 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1e6c64aa-4b21-385e-8ce7-39253cf8b798 | -10.21153 | -52.68419 | 2024-12-09 05:14:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4b0d721-db3e-3913-bdf3-89c111c67b32 | -10.84082 | -56.63232 | 2024-12-09 05:14:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 94813f93-734b-3181-9018-76e9b485dd9b | -10.38521 | -52.00111 | 2024-12-09 05:14:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49a30b2a-43a0-3d2e-9a3a-a4dce0415d74 | -11.87893 | -54.68149 | 2024-12-09 05:14:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81b35c05-10df-36dc-a0b0-6370a04b189a | -10.88361 | -54.75124 | 2024-12-09 05:14:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 924f977c-d217-393f-943f-08fe8fdb146d | -12.54114 | -57.74378 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ad3b8f5-ac6d-3a6e-88c2-2ab3bc7e19ca | -15.97716 | -57.17048 | 2024-12-09 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7f8b0670-4c4c-3f48-b693-a5669867cded | -12.84496 | -58.22296 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92d1fd1c-58cf-3136-a8e6-a88d833802c1 | -12.53778 | -57.74327 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3f469e28-3297-38d5-a2f4-8fc7554e8006 | -12.78656 | -54.22726 | 2024-12-09 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2e59482-c0a7-38d2-bc30-c7801e4a3cc5 | -10.42291 | -51.88867 | 2024-12-09 05:14:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca950047-8bb8-3f2f-ac61-cbd1d997c931 | -12.0512 | -55.46835 | 2024-12-09 05:14:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db096b30-1c20-3447-b0af-19905463347a | -12.54059 | -57.74741 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 29638829-73cd-3a60-8d8b-dff23e67be7d | -12.54224 | -57.73653 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 173c4b31-edbf-3fca-91f9-f6b2572adf73 | -12.53442 | -57.74275 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0fe65898-b425-3383-bcd3-7d737e2d1f38 | -10.96654 | -56.07492 | 2024-12-09 05:14:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bbcf12a-9bef-35eb-94ac-8adf4533cc6d | -10.83509 | -56.62371 | 2024-12-09 05:14:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 70ae9e33-1507-3fb1-b65a-bd6c54155301 | -11.61813 | -54.5343 | 2024-12-09 05:14:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcbea422-e939-3172-902d-fe6496654d0b | -12.85773 | -58.22863 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1670eae-0462-343c-a5ab-75a109c8a18a | -13.48125 | -56.55965 | 2024-12-09 05:14:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3883bda4-bb13-3d9d-a7f2-2b3ceb4b18e4 | -11.20938 | -53.82473 | 2024-12-09 05:14:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f703c71-5730-3bf0-8199-928ca6caf3d0 | -12.53607 | -57.73185 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 022525e4-5a7b-3959-974f-a99717140eb9 | -12.78323 | -51.50919 | 2024-12-09 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 716afc48-2aff-38c1-b885-00fdd06e88fd | -10.922 | -48.92812 | 2024-12-09 05:14:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27ed9e24-c741-3dee-bd01-1ef4ab1d9319 | -10.92155 | -48.9318 | 2024-12-09 05:14:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a829c050-a24b-3d3c-bd4a-a2ae610d69d0 | -11.28169 | -56.14472 | 2024-12-09 05:14:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8d52eaf-f46f-3d49-8a17-561077b53cce | -12.54169 | -57.74015 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4d88947-35ef-3796-bfde-619ccfd228f4 | -11.2101 | -53.81947 | 2024-12-09 05:14:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55c0f1c1-e48a-37e8-8820-303c63e4b8d4 | -12.53943 | -57.73236 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f95d005-0f96-3870-8106-fc08c240ff86 | -10.83795 | -56.62802 | 2024-12-09 05:14:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 97b26dee-ad6b-3fbf-8d9a-77a8fc8dd581 | -10.10481 | -57.85509 | 2024-12-09 05:14:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 849c6d45-66fe-37d8-826d-cba56f1dd492 | -11.74886 | -54.72769 | 2024-12-09 05:14:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e43e1a39-5172-3ce8-ade9-63b347e3045d | -12.53833 | -57.73964 | 2024-12-09 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 30fc1864-34b9-3b85-9212-d8f5084c6140 | -15.09162 | -59.63196 | 2024-12-09 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47cc5cbe-9c8c-36f5-a28f-e3c9d2bd61d9 | -11.7571 | -54.72411 | 2024-12-09 05:14:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6575d946-d15b-388f-858a-02debeb5133a | -11.88273 | -54.68204 | 2024-12-09 05:14:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb9217f0-1572-383a-aab8-92dcead164cf | -12.5305 | -57.7411 | 2024-12-09 05:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| f40d1afc-fac0-3ab0-b403-bc4b59512cd6 | -12.5495 | -57.7395 | 2024-12-09 05:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| dd9f3f1f-1b55-3bc4-8cbe-fdd341c1cc1e | -12.5305 | -57.7411 | 2024-12-09 05:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d181b2a7-cfb7-35f4-9952-8544037c498c | -3.2351 | -42.4353 | 2024-12-09 05:30:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| b33cc761-3ab0-3a21-a030-9f81c8b55aa0 | 3.63524 | -59.94751 | 2024-12-09 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdeda02f-5714-3851-8690-bd00312a60ea | 4.07813 | -61.15552 | 2024-12-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b74857f3-37f3-3be5-8681-c468d49dd73d | -1.61052 | -52.63332 | 2024-12-09 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c69959a8-f386-3b67-be64-84b4c101d2e1 | -1.60992 | -52.63718 | 2024-12-09 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad1963a3-ee8a-3938-a82a-18749b3719f4 | -3.46774 | -53.96495 | 2024-12-09 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6e481d8-018a-3182-97dd-c70e33623ee7 | -2.99947 | -53.0477 | 2024-12-09 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6ebc1d13-2fe6-34fe-b1fc-852782c59880 | -3.46471 | -53.96951 | 2024-12-09 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6fbf122-bac3-3073-a151-e0f901b8edd7 | -1.51483 | -60.33443 | 2024-12-09 05:33:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e21cf2b-258f-3b20-8bf0-4fad80682ab7 | -2.9938 | -53.04691 | 2024-12-09 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7c5ca9ce-e018-3e2e-87a1-e3dd1c7ef640 | 1.48467 | -56.04369 | 2024-12-09 05:33:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bd86490-b074-336f-8a16-682eb4194613 | -2.99892 | -53.0514 | 2024-12-09 05:33:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README13.md)
