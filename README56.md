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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e3b152e-5403-3f06-9c55-3ccc0ef275f0 | -6.12137 | -59.92882 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc907888-b784-3688-a21f-129d65a1407c | -6.78924 | -59.65628 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f86ec05-419f-3c59-bed9-fa3e5c39eb45 | -8.93753 | -50.16231 | 2026-08-25 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 131a3ba1-6598-3148-a497-8568b185b0d0 | -6.4452 | -54.96894 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1893b53f-d1f2-3675-9821-b60b31d94a29 | -9.39018 | -60.58131 | 2026-08-25 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32f7d178-a32c-3988-b367-74cff61a121a | -12.59039 | -47.9225 | 2026-08-25 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 756cdfa2-3059-3b20-b855-50d0e6d7102f | -6.15013 | -57.69336 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30b4a6a0-5560-3040-b81d-5c8709ea2bd9 | -6.14564 | -57.94083 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8591ecf3-a109-3ef8-a7c8-9b157de71d5a | -6.54298 | -55.0865 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6eb56b75-1cdf-3a4f-8f81-0a3106f7426b | -6.33944 | -55.87155 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4906d4a-88e7-3ccb-86b0-f1ed7c6e1a85 | -6.80165 | -59.60054 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6797c24c-2c2c-377f-b2b6-32db2ce108be | -10.43204 | -61.22746 | 2026-08-25 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 731a371d-4b6e-33b5-b3b6-a1e85baebe8f | -6.99708 | -59.2602 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| cefcf1b4-5705-3013-bbe1-a73ba0ca4183 | -6.54995 | -55.08756 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42dde39f-e316-3b87-943e-46f9b73a56ee | -8.54715 | -55.28893 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c8471b2-b2f1-32de-b403-e31637fc2d43 | -8.56168 | -54.71685 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6530137-b987-3c06-94e7-0b958093b0f0 | -9.16586 | -58.32984 | 2026-08-25 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 726fe158-657c-3c70-a5b5-13673f8b31e8 | -6.96212 | -59.07972 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e631767-1005-3bc5-81aa-d3575d9e030e | -8.20711 | -54.96989 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6118cf18-25b0-3088-9059-c87e97d9e6de | -9.2038 | -59.57532 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f99cd2b-d922-3816-866b-fd49a0612a7e | -8.56542 | -47.43282 | 2026-08-25 05:12:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5104796e-6876-3822-9db3-53cd6a899237 | -12.73512 | -46.472 | 2026-08-25 05:12:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 999ed165-adf5-39cc-a948-2159a0e4393a | -9.05911 | -60.43295 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b908c4f5-38f1-324b-872a-620abae6488e | -6.15282 | -57.93839 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f6b3362-dc56-377b-9f28-bab66d3d28f5 | -7.21016 | -60.6226 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d2fe939-30b1-3466-94d4-c8dc02e2fecb | -6.12411 | -57.83813 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f3e2685-e674-31d9-9857-5246197e0b9d | -11.15459 | -54.00061 | 2026-08-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3c111c0-f8d8-3fdd-bb73-1571afcd26fb | -6.35465 | -54.77852 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 069c7499-9b00-3274-bb84-3a39f3d71176 | -6.14682 | -57.69285 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a65d8b7b-5c4e-368e-84d4-ecfeff454c7a | -6.12494 | -57.74609 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dea291ef-51b1-3c10-96d4-9e7c9842b7b2 | -7.49079 | -55.35412 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd3bbba9-1ca6-3509-801a-97a5405ff16c | -6.99427 | -59.24831 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| aa43b143-1b07-3efc-8362-bf4baf486c8e | -6.61327 | -58.38346 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7957506-42e0-3a75-adc4-afb956f66efc | -13.35508 | -48.20682 | 2026-08-25 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c30c2c28-8841-3d9d-84b6-bd6abee953e1 | -12.11549 | -50.5775 | 2026-08-25 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0166a77b-ed9b-3fa4-b812-29f8ad46f9ab | -7.34913 | -55.65998 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5372926e-c6da-3098-8c63-319a860c0232 | -8.0808 | -44.64267 | 2026-08-25 05:12:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8260ed9e-a02f-3b55-9bd7-077e1575a22d | -15.32274 | -52.82048 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 192e4652-45cc-38d0-94bf-f0660c3100a6 | -12.95264 | -56.61685 | 2026-08-25 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4481c2b-ae97-30d4-840e-fdbe73fe7cca | -16.39024 | -49.91629 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffcc5a34-96cf-31da-8a2a-c88189b85fb3 | -15.86862 | -55.57652 | 2026-08-25 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab1f1e4e-6a40-3280-acfe-48a803f84085 | -16.42372 | -49.86583 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51602e13-d974-3fcc-9083-0a5667a50795 | -13.18797 | -51.49602 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7e55e157-fd0f-3e70-8d0d-fd2fb5f64697 | -14.30762 | -53.16869 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57de78f8-93b0-32cf-bc9f-3910f6c12967 | -15.31771 | -52.8244 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59e53b07-b9de-3528-95cf-88c8af97bb08 | -14.39229 | -51.77056 | 2026-08-25 05:14:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 55aa68cf-3600-31e1-af36-833cdc78a896 | -12.94789 | -56.61321 | 2026-08-25 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b451c100-24aa-3aec-aed8-8225629063cb | -16.41735 | -49.92569 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ea995ca-1efd-33fd-a4c1-28ef8f6dba1f | -14.40833 | -52.90094 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1d0e5e4-ad5e-3e45-bd8b-120482190c55 | -13.87181 | -54.04162 | 2026-08-25 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b066db1-ea96-3d86-8049-0df0f219c9f1 | -14.73178 | -47.15946 | 2026-08-25 05:14:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f06f7a2-9f06-3340-8117-b775b2cfbca8 | -14.36446 | -52.89486 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee2614a9-7c22-3959-bb57-2be35fff28b3 | -16.42263 | -51.84305 | 2026-08-25 05:14:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3378b4a1-de8f-37e0-b5b3-2bd25a4cae5d | -15.34903 | -52.79173 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fe68cdb-94c3-3771-8465-c2322602b815 | -17.31827 | -54.92467 | 2026-08-25 05:14:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 014ddfc7-86a7-3df0-9617-44ce3134fd75 | -16.40043 | -49.92493 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b835674c-016b-38ca-b9eb-56a5d24bab0f | -16.4233 | -49.86974 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26187b7d-22f9-3ff8-8992-8a33a884f9d0 | -14.79829 | -48.7954 | 2026-08-25 05:14:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16297840-b5d9-3c16-8cde-8bc7080be73e | -14.72592 | -47.1533 | 2026-08-25 05:14:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9319364-f4c0-3dd3-86e2-80d01e4e15a9 | -13.19651 | -51.39084 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 76a810da-fcf8-3d59-bf43-5e4b47707afa | -14.38842 | -52.95139 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46a7fcf4-c3de-3dac-a104-f62d060fd47e | -13.8768 | -54.03503 | 2026-08-25 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d37dd30-9abf-3352-9afd-421a091bc11f | -13.86453 | -54.00286 | 2026-08-25 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 369025d6-44c3-3716-b3d4-3c2dfa175706 | -13.87133 | -54.04528 | 2026-08-25 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b87bf24e-f4cb-3175-a1ba-8766c157bdd9 | -15.72198 | -47.66509 | 2026-08-25 05:14:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7373b35b-50c5-3a10-be44-fcdd7e622065 | -13.87322 | -54.03094 | 2026-08-25 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a4ea4d5-787c-397f-b72c-f03bea05aa0b | -14.35948 | -52.93409 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c5d9de2-a5f9-3d87-908e-2e120466aba7 | -14.36064 | -52.88975 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d278f5bc-0591-308d-965d-2d11bbd323a3 | -15.33949 | -52.7952 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9399335e-61a4-31e9-a43b-a1135a298b93 | -16.06687 | -50.46278 | 2026-08-25 05:14:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49a76346-0f55-3e9e-bb9c-cae6122ba098 | -15.27304 | -52.7947 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be50542c-dcc6-364a-ba72-a5820d9193b6 | -14.87194 | -52.67645 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ff844c3-141c-37f1-a209-c61bd7ac0458 | -16.50117 | -54.67024 | 2026-08-25 05:14:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e4ce35a-1dd9-3514-9e3f-e7f3963c2be5 | -12.94916 | -56.61633 | 2026-08-25 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2510184-afb7-331e-93ec-4ae94245cfd9 | -13.2042 | -51.48239 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5a1dd9c2-3f01-3970-bcbd-a3538dc90594 | -14.98287 | -52.68577 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc739eaa-71c2-3143-8ce9-b4f2ac841d77 | -15.32724 | -52.82078 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9d91a8e-97b3-37d8-b626-bee65562f002 | -13.87727 | -54.03152 | 2026-08-25 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0817b76-0ff9-3ae4-9c2b-fcc5efbba877 | -16.39962 | -49.93211 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4a495522-5aa6-3d95-9274-117e2b1d1947 | -14.54693 | -52.29674 | 2026-08-25 05:14:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f8ebfcc-ccf1-3098-962e-0e0256543ed7 | -13.9334 | -55.21849 | 2026-08-25 05:14:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5417cb1d-1e49-3b9e-800d-f6bee416926b | -16.40009 | -49.9308 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5bb6f0cc-be90-32bf-8ca2-190f8d425658 | -16.50472 | -54.67443 | 2026-08-25 05:14:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4098e65a-143c-3fdc-824b-8b823dbebb15 | -13.1924 | -51.38491 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 58029083-de56-3119-b91d-f5c9954fd34a | -13.6587 | -51.86282 | 2026-08-25 05:14:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8433daf8-81f6-3f17-ba88-a8a0f0daa682 | -14.4895 | -53.33641 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d9c70d6-7745-359b-9a8b-d61856d44aa2 | -12.95208 | -56.62078 | 2026-08-25 05:14:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c583e44-b400-37de-a903-f575109cbb05 | -13.40129 | -57.04742 | 2026-08-25 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0748009d-2f67-3d4d-98f5-63b32f2e582c | -13.18483 | -51.36775 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad93433d-3920-3285-9675-a1486653fa9d | -14.9106 | -52.64258 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 746db732-3fc9-3503-b345-7598a54f650f | -16.5007 | -54.67382 | 2026-08-25 05:14:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9c1bc6f-9388-31a3-af89-4b0f1993e822 | -16.39062 | -49.91483 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b9a111c-8ea6-39e9-8c5e-fd2635ab2b47 | -13.17113 | -51.36049 | 2026-08-25 05:14:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3329d140-26d4-3341-be40-71edacd7a5cd | -14.40891 | -52.89651 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75d3cc28-2fb9-3c86-8c7f-0378083ec735 | -13.45663 | -57.05117 | 2026-08-25 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8f3fb64-3fa6-3a31-a1a5-45d8ace433ae | -16.41147 | -49.92862 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4bdaee4-b934-3d3f-af9c-888da9a652a1 | -14.36009 | -52.89417 | 2026-08-25 05:14:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abc4447e-8ad4-31e4-b204-ccf0f8746c70 | -14.97839 | -52.6851 | 2026-08-25 05:14:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df6ef27e-adc0-39d8-9ca7-86ec07704a69 | -14.25518 | -52.12825 | 2026-08-25 05:14:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d46c73ea-4465-3c88-8277-9189588de726 | -16.40597 | -49.92791 | 2026-08-25 05:14:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README57.md)
