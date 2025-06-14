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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e61d3066-8296-3aec-aef6-5d1c22ec569b | -10.80828 | -56.94521 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87e52b6d-bb4d-3762-ae64-609c987a0d27 | -10.75752 | -54.78334 | 2025-06-14 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d007c70-7b6f-346c-8868-a5f505a3c2de | -10.2927 | -60.55183 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24ebf882-a669-3fd5-b8a3-86d8c5bbe819 | -13.89911 | -54.62024 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d473b6c-7244-30a1-9d3b-1dd90fde4baf | -14.21228 | -57.41203 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c114290c-343c-3a1a-b232-824fa2733ac4 | -11.80637 | -57.35135 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a98251f3-8ce9-32da-a260-a91538fccffb | -9.25123 | -57.53743 | 2025-06-14 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 106d9fb7-7dc2-3ba5-a410-6aad38ffaf2e | -12.28279 | -57.26344 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e609aeb-1d13-3ba4-ae79-6e45cdf6b628 | -13.49883 | -53.48622 | 2025-06-14 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 640a8e94-4b4e-3e56-b6dc-72d0f74bc011 | -10.9433 | -56.84236 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 541d8d7e-54a7-3da4-9c9b-d054fecea5a9 | -10.92276 | -54.78139 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd053e9f-2c64-34ba-ab9b-844f18e6beac | -13.58623 | -54.28693 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 32f89dfe-bde4-384b-94ea-7a1d2e8078ff | -12.62 | -57.88838 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d59e43f-0584-3278-bc24-099a387c71e4 | -13.89973 | -54.64161 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7884a013-e8a8-340d-98b7-1f2bf19e738a | -10.86511 | -54.29633 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f969b39c-f4d2-3e6c-81ae-386e423672bf | -9.92022 | -59.90898 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 176347c5-d5ae-3473-87f2-3683d97f360d | -10.91933 | -54.78085 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5953e96e-e058-3e66-b79b-272797e20605 | -13.51163 | -55.65514 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87f80c37-8b4e-3364-9d1b-dff52fda39ee | -13.89838 | -54.60488 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| af691b97-9aab-3f2a-ab17-b5461d0db77c | -13.22775 | -49.83261 | 2025-06-14 05:06:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0f84d474-d911-3505-be45-ffc198dd1034 | -11.88335 | -54.68081 | 2025-06-14 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d6f6b68b-7372-3678-a241-6f4b274a0a4f | -9.84594 | -63.66792 | 2025-06-14 05:06:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f29515e-c75d-3f8b-9ddf-124061ded8f7 | -11.80747 | -57.34435 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd30f6fc-642e-3d5e-bddd-600b2aff33da | -11.81022 | -57.34838 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ccfeb69d-ee9b-3dcd-b4a8-641a95933200 | -10.92047 | -54.77325 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4f64086d-4517-3acf-81bf-d89ca7db1e40 | -10.02028 | -57.32616 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f4ab185-4d7b-3522-aa73-464448247072 | -12.6862 | -52.39663 | 2025-06-14 05:06:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 223f2b79-3a87-3e4a-99ad-6cb3815f349c | -12.61395 | -57.88377 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 616fbb57-74c1-30f7-ba69-cb1cfe45bf05 | -11.01397 | -55.08701 | 2025-06-14 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 39122d40-b3d2-35e1-895c-640345738a08 | -10.87444 | -54.30588 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66c73c1b-233e-308c-991f-8153e1c0d657 | -12.61726 | -57.8843 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4047b9ae-dded-3fe5-82d4-8a5741c06866 | -10.62114 | -52.58718 | 2025-06-14 05:06:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba2b54b5-c69f-312f-86fa-98d88513080c | -14.21668 | -57.40549 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fc5e2a5-a4e7-3065-86b8-3191f1dcb377 | -13.96458 | -54.44165 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 755957bc-e940-342a-ab04-d2b71d235140 | -10.75465 | -54.77902 | 2025-06-14 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f5b5f5d-563c-3f70-9bdc-c6cf26476cf3 | -10.9235 | -56.8392 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bb554b81-8914-3561-9f92-555f7b4998e8 | -14.68167 | -53.37159 | 2025-06-14 05:06:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa2a688f-219a-30c3-a342-9877b9e73b09 | -9.64285 | -67.2889 | 2025-06-14 05:06:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ef9f1e2-3bf3-3130-9b16-88cd15dc98e7 | -14.20898 | -57.41149 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b480a482-d9bf-310a-aa7f-59eb3710701b | -10.85389 | -53.78496 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 544c2c48-3148-3d91-8488-e1a60e00109a | -10.85328 | -53.78912 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cb2eb10-1cb1-3ce0-bb10-b941d7acbab4 | -9.40044 | -65.51317 | 2025-06-14 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7334ef9a-f337-3a75-b755-671187a8f4d9 | -12.16315 | -56.54508 | 2025-06-14 05:06:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b719128-8ffa-384d-be93-0ad756da564f | -15.39362 | -47.86451 | 2025-06-14 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d47d40c2-5263-3333-9f30-a0e050bd377b | -10.29508 | -57.13779 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 968d379d-856b-3ce7-8066-3e02dfc16fd8 | -11.81155 | -54.50454 | 2025-06-14 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b0e0545-9916-3183-a1d1-b1c855393969 | -12.21318 | -49.64337 | 2025-06-14 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ea4d23b-0132-3348-b83e-2488fcf7db63 | -10.8545 | -53.78082 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bfc1d87-ef51-33ab-af77-83abaf916c58 | -11.80967 | -57.35188 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ff80bc5a-9313-3867-ab14-5856bfc37440 | -14.21614 | -57.40902 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 780ac5e7-8969-3b41-a0f6-daa1cd909e19 | -13.90133 | -54.60961 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e150e7c-95c7-3850-b967-1890d6815f97 | -10.93725 | -56.83782 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0aa30f85-8d81-325a-9b39-ed33ed988abc | -13.8997 | -54.61604 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a038660b-f7a4-37d8-b299-aaaf96e75b17 | -11.91798 | -57.46281 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03426c60-f3b8-3dd2-ad28-d678e0de9250 | -10.92123 | -56.78877 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6fc39d4-09cf-37bd-8bf2-8bee32210e77 | -10.56433 | -52.01724 | 2025-06-14 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e7d8957b-162f-3e77-9536-8ca727c0518f | -14.53756 | -46.02953 | 2025-06-14 05:06:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5ce201d-0c5a-3eff-9eb5-370601f435a9 | -9.47046 | -57.85081 | 2025-06-14 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 00fa952a-9c80-35d4-9d01-01ec9db995f2 | -10.93231 | -56.84776 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35302ffb-36e3-34b3-ba04-f6595ec1303e | -11.91743 | -57.46631 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bddc19a-e4fb-3f49-9508-1d54205c3869 | -13.89777 | -54.60908 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 51a996bf-3f6b-35ad-a3d7-429727c9471d | -10.92405 | -56.83571 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fe6c7ddf-3bdc-3320-b8bb-25016474d19c | -11.91578 | -57.47683 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1e70450-b008-320e-8446-edaf98aaa98b | -12.51538 | -57.18999 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98e0b13d-2e81-3644-aa9d-73ad9e85abfd | -14.22109 | -57.39894 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 634158f2-c439-3893-aefb-bb7d9e48074e | -13.89715 | -54.61328 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 56a445ca-277f-3fcc-bdc0-a17a0c512c01 | -14.22274 | -57.4101 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 677fb74d-a031-3cab-a591-1165c6f415af | -13.90029 | -54.61184 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 52ccf9e0-694c-31cb-af12-13515ce619c3 | -10.94 | -56.84184 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9d77e6a2-920a-3d7a-9f50-48202afd9780 | -15.39489 | -47.86371 | 2025-06-14 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34041056-37c9-328c-85c0-a565f29553ae | -10.94109 | -56.83485 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bd8878c-45e1-3e1f-8814-57ed22b373a9 | -11.91688 | -57.46982 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d75f5ca0-e19d-325d-917b-bc31ab65aee8 | -13.36581 | -54.26073 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92b0f25d-a7b9-3110-ba06-9e4a47272c0d | -14.21944 | -57.40956 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa316f7a-5e4a-3b7f-84de-cf2bf3c8fe17 | -13.89593 | -54.62165 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bbbd5d7-07d2-3d12-ac23-4df9e7866d7f | -10.93449 | -56.8338 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9b3f159-5c36-3d61-9d08-605c849ecf1f | -15.39759 | -47.8898 | 2025-06-14 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d2c0b3d-8a77-37db-bebd-98af3b16af9a | -13.96877 | -54.43801 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbd8cf04-dc42-3a02-9c0a-cd681ef4c1d6 | -15.39963 | -47.87184 | 2025-06-14 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b257853a-cfba-374c-8c2e-31c995b39d7b | -10.29641 | -60.55249 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c8021a4-15d5-37c0-8789-2a58389f541a | -10.26229 | -54.99719 | 2025-06-14 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d91ac5d-8c76-3d6f-8888-91de24c2d64c | -11.13376 | -53.94604 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2243b93b-b552-3199-a37d-77bab75c81a9 | -10.09292 | -52.74215 | 2025-06-14 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cec6b48a-d256-35ef-aac7-f38551b9bb92 | -9.92454 | -59.90537 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3af84af4-87cb-3507-8f3c-75156beb0621 | -13.9649 | -56.78905 | 2025-06-14 05:06:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32b83e06-f7b1-345d-a837-24886e60cc1d | -11.01056 | -55.08649 | 2025-06-14 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f7ed8e36-f630-3341-850b-ae2bd48be726 | -9.46434 | -57.84612 | 2025-06-14 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1530d0b0-a648-3aa9-95d9-d77310090cb8 | -10.3693 | -57.22845 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60ab360e-18b1-3016-8e7c-a518071b3bd5 | -10.94276 | -56.84585 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9f085e97-4a32-33bd-9bbb-43b1939e748e | -11.74832 | -54.7164 | 2025-06-14 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce355854-4311-3278-a066-3ddf6b9cdc91 | -11.76973 | -54.36861 | 2025-06-14 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2eaabd23-c691-3d1b-b81a-b7377c4110cc | -11.88393 | -54.67688 | 2025-06-14 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 281134da-6d61-3dff-a244-2a2a56959412 | -14.53676 | -46.02668 | 2025-06-14 05:06:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d14c24a9-6337-3842-8d6f-51f93017957f | -10.29938 | -60.55751 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e799dd4-109b-38ac-8b37-60674f3b2115 | -12.62056 | -57.88485 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03661cbd-8660-3194-90a7-f97c13d4d001 | -10.94439 | -56.83538 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d31936b2-1e66-3176-8969-d2e8659fec4d | -15.38379 | -47.86162 | 2025-06-14 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 088e36ba-4123-3ab9-9b85-4cf8225b9b1b | -12.62662 | -57.88947 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e3705a1-a0e3-354c-b1f2-86476201d514 | -12.62387 | -57.88539 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09555953-8166-330f-a28e-b57fa9ebee2d | -15.99123 | -49.81791 | 2025-06-14 05:06:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README20.md)
