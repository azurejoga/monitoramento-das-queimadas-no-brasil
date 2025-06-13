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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67211bc1-2904-3557-8aa6-69af307e1868 | -16.14421 | -60.0889 | 2025-06-13 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cb9a43d-faa2-38ff-8b46-8c09e8501a4a | -13.58924 | -54.27943 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e10b3f32-aa84-37a8-abe9-b36723bd7ae4 | -17.37902 | -53.82102 | 2025-06-13 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20720e50-fbc7-3cca-9bc4-aa7c837c75fc | -14.68318 | -53.37439 | 2025-06-13 05:25:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b0e1952-17e6-3012-b098-ac5d2f8ce53c | -13.89438 | -54.61757 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6ea8c664-01a0-3ff0-83bc-b30a03e4435d | -12.47081 | -58.47147 | 2025-06-13 05:25:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3981ac1-22c4-3c45-806d-bed5d3139edd | -19.7011 | -54.61652 | 2025-06-13 05:25:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69022e5b-69c4-380a-b034-ff32bda81008 | -12.51824 | -58.3449 | 2025-06-13 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edb47385-f00b-3ed4-8a26-314229d8424d | -12.47448 | -58.47201 | 2025-06-13 05:25:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b767d37b-7b6d-3e6f-ad10-3a6363dd35e8 | -14.04047 | -55.13544 | 2025-06-13 05:25:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a2f7fa3-72b0-3141-94c6-c4e0a541331d | -13.90265 | -54.6296 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 045852eb-0679-357c-b0ef-19d094ffb371 | -13.90133 | -54.64037 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c80f2cae-eb3d-3410-8c20-f63df8e841a6 | -12.70414 | -58.0348 | 2025-06-13 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e878f0aa-a547-3bcd-b9b1-c39ebe5e9aeb | -13.09166 | -52.28517 | 2025-06-13 05:25:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3b8f133-6bf2-3f12-a868-d3d92591b1c3 | -13.89719 | -54.6344 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c7d3426b-526d-3687-8ffa-d586a6abaf21 | -12.43444 | -54.87735 | 2025-06-13 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c2875e9-5a29-3ff4-b5eb-3852a49b0e81 | -14.67793 | -53.37359 | 2025-06-13 05:25:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 670dd810-11e9-3737-8d3f-4eb84e50d695 | -17.38371 | -53.82007 | 2025-06-13 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 097dffd5-e80d-3146-a46a-ebebad611dc3 | -11.67903 | -62.26315 | 2025-06-13 05:25:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6e240e16-d008-3ce5-af4a-69f7f306218d | -12.52256 | -58.34102 | 2025-06-13 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 128897ec-5d42-3542-b1f3-653f1fc9b574 | -13.89305 | -54.62846 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 48ab403c-b258-302b-882e-eacad87feea0 | -12.52676 | -57.23658 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b4bee1d-d05e-37dc-8190-3c4e5d34b1fd | -13.97699 | -54.45362 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abed2651-d4c6-3909-9961-3237ae71df0e | -14.19169 | -57.4076 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7613ee4-9f68-3132-af94-9c9568a1b4b2 | -13.89372 | -54.62302 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 135fee02-6dd0-39d5-b2c9-fdedfb01424a | -19.08077 | -53.46881 | 2025-06-13 05:25:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a084830a-52a8-3ab9-9bb3-0985bdd5357d | -13.29013 | -57.06832 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a203b6df-aeee-35e5-a459-2eaa5194b61d | -14.20017 | -57.4051 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 299553d4-cb50-36b2-b737-14186108faac | -13.97439 | -54.44696 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e0e45e9-d7ea-3394-8c91-f7a2e2e71e4e | -13.89918 | -54.61818 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f52ebaca-80a0-3c2d-933c-3d2371a37e1d | -12.43048 | -54.8718 | 2025-06-13 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ab6ee20-9eab-3df5-b3e0-17f142e0bce3 | -12.51815 | -57.24054 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 654adb4e-476e-32f7-b5f0-f0eea0e19a71 | -12.52626 | -58.34156 | 2025-06-13 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fafcf2b6-5cc2-3dba-9c97-68b54ff9d0f4 | -13.58605 | -54.28283 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d43cef9a-57fd-3bd7-8821-cfa566632271 | -19.08115 | -53.4651 | 2025-06-13 05:25:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4d1141e-7b77-3678-b3c0-ff69bd9b6b5e | -14.21264 | -57.40329 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 149de677-7330-3480-a7f6-20979d92919a | -12.43028 | -54.86813 | 2025-06-13 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86eaa98b-22cd-30c9-9eff-a45b38b20fb7 | -14.03242 | -55.12417 | 2025-06-13 05:25:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b0a1db7e-78e6-3bb7-9781-65646b68f82e | -14.20417 | -57.4057 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3ced3e21-0947-3bd0-973e-511402000166 | -13.98316 | -56.0158 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0968d5f7-a8df-3932-a724-22e2ee233986 | -14.20914 | -57.39905 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 109e456c-82e0-3800-b20c-615c918e5128 | -13.98754 | -56.01631 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 573bf486-9d8b-356f-8b1c-ec0ae091e8c4 | -12.47513 | -58.46758 | 2025-06-13 05:25:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3154351-d4d9-324f-8304-69302fe6e1c5 | -13.28963 | -57.07196 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 778048d7-7d6b-3091-8c40-509f3670f304 | -19.70145 | -54.61323 | 2025-06-13 05:25:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a351da3b-4f6e-3716-a351-611f25de89fc | -12.52353 | -57.23083 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03abadb8-af27-33b4-b68b-53b2a8ac0bdb | -6.71985 | -55.33507 | 2025-06-13 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72fa9297-dc4e-3c2a-bf5d-28df2bf94730 | -13.97854 | -54.45319 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3d634d04-7fc4-3b24-9ec8-6099c252bde5 | -13.89654 | -54.6397 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d4908463-8485-3692-a211-f6ffcaed6279 | -14.20864 | -57.4027 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8a7663ca-e57f-3c82-80e4-1852e30caeba | -13.89176 | -54.63905 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 75b2744f-b194-3860-85df-58ee5a8da31f | -12.52194 | -58.34544 | 2025-06-13 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c53291f-96ac-3861-9d6a-aabe15c89f1f | -13.89851 | -54.62364 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ec09dcf7-2aa3-3196-a0d9-2a9463c56a08 | -13.97764 | -54.44814 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5affd4bc-41d5-35cf-a52f-0b2b8ca4f2c0 | -14.21313 | -57.39963 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 798b0482-e5f2-31ca-a6ab-9ec5b030048a | -14.67903 | -53.36393 | 2025-06-13 05:25:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c68d1da8-883a-3a9c-ae7f-4420e9736230 | -14.0411 | -55.1304 | 2025-06-13 05:25:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf21ccdf-3018-3565-8718-43d7ec7a8997 | -13.25028 | -56.53458 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e158a56-c538-3647-9944-4a44073702d6 | -12.52281 | -57.23599 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8946eb49-82ae-3ba5-8320-e4e7d9df82f1 | -12.70791 | -58.03538 | 2025-06-13 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb1f807c-44c2-34d6-9e9e-f42353dfbd2c | -14.20066 | -57.4015 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7df77fab-b805-34b8-a0f0-db4798053aa3 | -17.38431 | -53.82174 | 2025-06-13 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 481e7564-b29d-361b-aced-99973dadeec0 | -11.68295 | -62.04459 | 2025-06-13 05:25:00 | NOAA-21 | NOVO HORIZONTE DO OESTE | RONDÔNIA | Brasil | 1100502 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebd6b72a-b84a-3908-a2c2-8f121f7e2cae | -13.90332 | -54.62419 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d0252055-deeb-3a47-85f3-7fd101265776 | -13.90199 | -54.63498 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b09f673e-563d-3ea4-9d01-99d4309a24d6 | -7.24101 | -55.41256 | 2025-06-13 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b79e97c-e8b7-3d42-87e1-6d5e4c96a56d | -12.47146 | -58.46703 | 2025-06-13 05:25:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36991726-4be8-3e8c-b8f8-8f5a78915d41 | -13.90067 | -54.64577 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ff0e43db-85f1-3c95-a9dd-c7113a9b42be | -12.43509 | -54.87244 | 2025-06-13 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38ee55a5-4db3-3843-aa31-4da3d3e80424 | -21.67441 | -56.62862 | 2025-06-13 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1311e311-c1eb-3017-ba3c-b7a547908530 | -21.67161 | -56.6273 | 2025-06-13 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5222c8b1-b06e-3b06-aa60-573cb9754a32 | -21.54114 | -56.05062 | 2025-06-13 05:27:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80f60f54-c30e-359a-8d7e-05e2a085f879 | -21.17693 | -53.29934 | 2025-06-13 05:27:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38229574-99e0-3d98-893c-f462ae7f324c | -10.9355 | -56.8322 | 2025-06-13 05:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 65dfc425-ff05-31c2-a544-d199c2e9d165 | -13.8867 | -54.6312 | 2025-06-13 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 41.0 |
| dfab74f6-02d0-348a-a4bc-3b7957c96bb5 | -13.8867 | -54.6312 | 2025-06-13 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 2433ce6e-0e54-3d28-8067-0fcbf7f66c48 | -10.9355 | -56.8322 | 2025-06-13 05:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 401cc588-0dac-33c5-989a-bf9f5f512941 | -10.9355 | -56.8322 | 2025-06-13 05:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 88e9a7d5-5066-3616-84e8-96f9a16e7215 | -10.36698 | -57.50109 | 2025-06-13 05:50:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edf62f95-7941-3d22-b5d0-8fa48f759772 | -8.68215 | -64.86914 | 2025-06-13 05:50:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40582e90-cfa5-3417-9f79-305dd93a94c1 | -10.29587 | -57.14156 | 2025-06-13 05:50:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b38770e-9ff4-3c65-bf07-5f14aa395b24 | -10.36502 | -57.23804 | 2025-06-13 05:50:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9f1cb09-8185-3d10-aa90-3489be4f4960 | -10.36555 | -57.23386 | 2025-06-13 05:50:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b86e841f-6ae5-315d-8d8a-aab4b4d19ee2 | -9.40214 | -57.55077 | 2025-06-13 05:50:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 39155a89-d070-32f0-bb80-f8c7a1fdc6ef | -10.36663 | -57.22526 | 2025-06-13 05:50:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 231cd78d-f8cc-3516-8568-7414f201d200 | -10.36726 | -57.50292 | 2025-06-13 05:50:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4db8611e-3d7d-3915-a65b-9f3ed378d987 | -9.88361 | -61.39653 | 2025-06-13 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6536914f-fc71-3d9d-8f95-6bfd12dd2d81 | -10.86289 | -54.29816 | 2025-06-13 05:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52e3420c-09fe-3a1e-8fa5-f2dc43f52594 | -9.22166 | -62.47289 | 2025-06-13 05:50:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3119d2ca-3a1b-3931-af49-419acd9b4597 | -9.24972 | -57.53731 | 2025-06-13 05:50:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ceddb0cf-3081-3dd7-82f8-281117c3fedd | -9.22218 | -62.4693 | 2025-06-13 05:50:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b77ae6e1-72ba-3fc1-96a3-e7b96312f6a2 | -10.36608 | -57.22963 | 2025-06-13 05:50:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b653b0b9-02a8-3b5b-90a6-809c80d9b59b | -9.40782 | -57.55161 | 2025-06-13 05:50:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 35589c70-7efe-3812-ba88-d4401d657b9c | -9.8786 | -61.40025 | 2025-06-13 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6032945-0aa4-3334-9b49-7dbf6240ba7c | -10.29924 | -57.13963 | 2025-06-13 05:50:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12d8c8b5-f2c5-32e4-a789-8333a4a4ea52 | -9.8792 | -61.3959 | 2025-06-13 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaf168c5-d609-31a9-b0d1-4783ce191d76 | -10.36677 | -57.50694 | 2025-06-13 05:50:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8d54245-233b-3926-bd30-105b6c7dc9b8 | -9.40612 | -57.55341 | 2025-06-13 05:50:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5a3daf03-6595-36ff-8ee0-ab3aac23741a | -9.40664 | -57.54953 | 2025-06-13 05:50:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c3a6bd4f-2e6a-3a5a-a919-68107a8f8297 | -10.30178 | -57.14229 | 2025-06-13 05:50:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README22.md)
