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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0696c91-146c-37fd-a62d-7f8d688b104f | -12.80347 | -48.41473 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6fa7c514-8263-337a-8f38-b2cae97730e8 | -14.57176 | -52.99261 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0a20ba8-e64b-31c9-b9ef-b01bc27d1abc | -15.49333 | -53.90008 | 2026-08-21 04:49:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ce4a0b8-cbb2-3870-9f3d-c18639e1f68a | -14.31606 | -51.89598 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 12852908-9fbf-3caa-9e77-cb00de461317 | -12.72882 | -48.47937 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6105af0c-8d8f-36fc-a9a4-444c2fbcf10a | -13.3946 | -54.3749 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 50527a44-a388-3b14-9431-a1678f580e4d | -12.25599 | -43.17377 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 54a81be4-f9ca-3470-b5f2-1216f00ae137 | -14.07949 | -58.8725 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 325cd463-196f-3983-9f4d-8aaeaa2ed0b2 | -12.2449 | -43.17561 | 2026-08-21 04:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 36ebf914-a243-3c14-91ff-51f26addbb13 | -11.18061 | -54.00945 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 806578e3-555c-3d25-a394-968bcb970968 | -14.33626 | -51.91439 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a646aeb3-6e22-3481-9861-07171c60f3b7 | -12.78627 | -48.39865 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 04028ad9-960e-3525-a50b-33b1cac2fe82 | -13.38389 | -54.36974 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| c7406232-b6c8-3631-ba22-2e00e2185ab8 | -11.20223 | -54.00539 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57085034-9b5c-3708-9a5d-a1c58244870e | -13.39799 | -54.37547 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| da3cd5f6-5466-3bac-8d79-4e0b78cd7dd9 | -11.1726 | -54.01574 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 36740aa2-7d87-31c2-a23c-3f3599e9b075 | -13.39738 | -54.37918 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70a59472-ed17-3bc6-bb8a-3c73956f8d2c | -11.18098 | -54.02863 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e7efdb2-b7a0-3470-b439-615bff03dd75 | -12.00041 | -53.4258 | 2026-08-21 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e542bed9-6b21-384b-bedc-9b3e78122c37 | -14.02407 | -58.86713 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8924e7f2-488f-3f97-90f6-681e621bf926 | -14.20104 | -52.88458 | 2026-08-21 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9056eb3-dc58-3bf3-8859-952ceb619da7 | -14.23205 | -51.93073 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c8104bd-3bd7-32a0-b620-43aeb5fd05bd | -12.80414 | -48.40991 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 25d609f9-6e19-3184-a434-bd5d04f09d10 | -13.44486 | -43.83968 | 2026-08-21 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f82f7cc3-e6f4-3fee-aa90-009605bc0e17 | -13.38599 | -54.38496 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6eddcd03-2d37-3014-9d79-f1ba3888fb59 | -14.31839 | -51.89663 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 466c5ed6-2497-336d-96ed-0806c86d185c | -12.52505 | -52.44818 | 2026-08-21 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2312b565-ba41-3a0b-ada5-7522ecbe968e | -12.91145 | -56.63015 | 2026-08-21 04:49:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 184c4551-9b2e-3d51-b196-afb933447538 | -11.18681 | -54.01428 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edcb7b73-a044-3cb7-b55b-850cfe3dd5d9 | -13.3793 | -54.37663 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 44f2068d-63b0-3f59-a5d8-d15ea9cf6863 | -13.43794 | -51.79483 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c619928e-7107-34fd-8b75-f38153548220 | -13.43853 | -51.81336 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4179c96-32a1-3ee5-a621-b96cb3d2cc73 | -14.90582 | -44.8058 | 2026-08-21 04:49:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6473577f-0fd1-3642-a7ee-63681598206c | -13.39277 | -54.38609 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e8ef7b67-2cbd-3c86-992a-2e4915b348e0 | -14.2016 | -52.88103 | 2026-08-21 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23258808-0971-3b01-9cba-31a7f2c6f4a1 | -15.15489 | -48.69133 | 2026-08-21 04:49:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ed2864f-ef3a-3d25-9fea-76927f003898 | -15.7136 | -47.79587 | 2026-08-21 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcd910f4-f747-3766-8e92-d3061a1ec55c | -11.17076 | -54.02694 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 11ae2dd0-5946-355d-b9fb-45e1a8afd6db | -14.57838 | -52.9937 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e980b5f2-6377-377b-a0e0-4ed6c2cd13fa | -13.7408 | -51.8573 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0f8a4b2f-b11f-3183-8fb7-8afb3aa40251 | -12.51994 | -54.75842 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0782e099-645c-3530-8a96-be6dc9335536 | -16.57092 | -49.40271 | 2026-08-21 04:49:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d071303e-b556-3b70-a52e-ec9dcc2a0ff8 | -12.76116 | -48.46968 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 004b5c70-d695-379c-b78b-ba8e33607d6b | -11.1766 | -54.01259 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37658ff7-6bbe-391a-b75c-27f3c06c34b0 | -11.67966 | -54.56928 | 2026-08-21 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f50b1080-ae20-31f2-bb02-ca8149d7fc8d | -14.33905 | -51.91856 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19ba4bc9-37b4-3d05-a036-c80de1b5ce8a | -13.74359 | -51.86142 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 079652dd-979f-3de4-9729-125663164ffb | -11.23792 | -54.82682 | 2026-08-21 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f67482a3-d0b0-3400-87b0-519933bf8e0f | -11.17138 | -54.0232 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 596b2aad-17be-386b-8d44-e39bda951230 | -12.75052 | -48.46158 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df2ad686-6a9d-319d-a78a-19baf9d91d83 | -14.5519 | -52.98935 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9e3e027-8691-38b6-9e25-922dada0944f | -12.51523 | -54.76555 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a01c4c92-0a84-3d33-96ed-0db31693852b | -12.78615 | -48.45581 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a4b71ab7-34a7-3cf4-ba6e-d5fd7c54e775 | -14.22312 | -51.9219 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d20cb17-fd45-3b82-bad7-35cf21873764 | -15.44739 | -41.38905 | 2026-08-21 04:49:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 5d209f1d-e9d6-3e2e-82e7-9b59828b030b | -13.59077 | -51.81473 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3a1d6a4-1806-3bab-8b41-c9270d7ab6b1 | -12.83739 | -48.44983 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1adeda80-9b60-36e2-9d3d-3cc7466bb07e | -12.51931 | -54.76228 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81ee2f6b-d0e1-3087-a043-def5bd9c8319 | -12.8966 | -53.2005 | 2026-08-21 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7afcec28-0f29-336e-b367-096fa21b2cc1 | -12.75496 | -48.45737 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04f1cde0-edfb-310d-9987-8b53d41da83f | -14.93451 | -49.0048 | 2026-08-21 04:49:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3d603b9a-5c88-339f-a4f3-467c33360e8e | -11.18401 | -54.01001 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1e0ca3f-2115-3ec8-89df-1799be87ff1d | -12.84566 | -48.44629 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32d8bd53-56fb-3d90-841e-d503be9d1ee7 | -12.50894 | -54.76056 | 2026-08-21 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca6201a6-f64e-3b7d-9462-ed4fc8427cd0 | -14.15563 | -48.35818 | 2026-08-21 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30033ff6-c07a-313d-bef8-a09ca194a310 | -18.02824 | -44.61181 | 2026-08-21 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1b06c1dc-1a0a-3c90-890e-39ab1dd4aec7 | -15.01588 | -52.67104 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffafd985-7aad-3e72-aad1-50bfbfc73f5e | -15.00097 | -52.67957 | 2026-08-21 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 624f37da-f418-38db-b9e0-027dc2da5d98 | -12.84328 | -48.43561 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d1a45b7f-e347-39f8-9d52-123a1342167c | -12.83667 | -48.45501 | 2026-08-21 04:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c42a658c-4231-3d7a-9201-3c87cb5afbd8 | -11.17015 | -54.03069 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0a7b1dfa-b7e2-352d-a40d-e4b721c35d2f | -13.93507 | -53.85673 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 83e479c5-560e-3121-87a8-9863fbf91eba | -16.57157 | -49.39791 | 2026-08-21 04:49:00 | NOAA-21 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 66e92268-df15-31d0-96a5-e15ffe918a26 | -11.1856 | -54.02172 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da9eccd6-c058-381c-baed-2058840e2f1a | -15.55451 | -50.27946 | 2026-08-21 04:49:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab1f4fac-49da-3914-be71-943242cf113c | -14.30938 | -51.8949 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5631e12c-3fb7-3096-b150-12e057611805 | -13.68169 | -48.76436 | 2026-08-21 04:49:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 755107d8-16da-3794-9da4-116de1075067 | -14.09811 | -58.81789 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e60d065-186b-3923-9825-7da721c6e61e | -11.66479 | -48.35101 | 2026-08-21 04:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67f07163-2673-3c77-afec-5e3509a34baa | -10.39485 | -61.20515 | 2026-08-21 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bce0c5c-7f8c-3fe4-a19d-53102bf56712 | -15.60122 | -46.57508 | 2026-08-21 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 43bbe631-123f-3197-97b5-bea81b32f82a | -12.80027 | -48.40986 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be804d39-5083-3712-ab4e-1a7c42b8897c | -13.43629 | -51.80564 | 2026-08-21 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de7b2266-85bd-3b8f-a3f3-51a9efe18cbb | -15.54797 | -50.27421 | 2026-08-21 04:49:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae1ed5fe-7bad-32e3-b095-a9f60a2f6695 | -14.55022 | -53.02186 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e456327d-a6b4-349e-b6ec-b10de332d9e0 | -11.16797 | -54.02263 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| afacb5d8-8109-3c0a-b339-45753491f08f | -12.74855 | -48.44948 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9473f7c4-0abb-3a74-ad77-da284e0916f2 | -11.16518 | -54.01834 | 2026-08-21 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7b2adb66-0eb4-37d5-988a-8d6745530b58 | -13.93231 | -53.85258 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1e661fbb-db24-3eac-8938-9cf0f3430025 | -13.94509 | -53.85838 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db3cb357-86f5-3121-9858-07b2df9a24b5 | -14.31852 | -53.45726 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39323c3b-67e8-305f-9162-022b42cb3db0 | -12.74101 | -48.44802 | 2026-08-21 04:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6af459a2-a941-3366-ba07-0716637b7caf | -14.28331 | -47.42273 | 2026-08-21 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b683b6a5-0488-3645-9550-6757bb8c857d | -13.94843 | -53.85893 | 2026-08-21 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e12fe0b-2bc1-30d9-b683-fc256cff1559 | -14.52635 | -53.1745 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7063a59d-7c95-3dfc-a810-3dece3c8e56a | -14.54746 | -53.01777 | 2026-08-21 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| beca8fe4-aa43-38eb-a898-78e6c297abc0 | -14.31327 | -51.89181 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0ac2ddeb-6be4-3674-8ead-09e156b4444a | -14.30993 | -51.89127 | 2026-08-21 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4635a7fc-a94c-3072-8292-a206a7e53836 | -14.11629 | -58.83789 | 2026-08-21 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9270a40-308c-3a9a-96ba-0add8d6fe133 | -11.20133 | -55.05155 | 2026-08-21 04:49:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README52.md)
