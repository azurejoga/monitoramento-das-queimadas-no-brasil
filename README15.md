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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c67e8feb-0420-39ea-a065-99449b97e4c4 | -7.2187 | -55.0815 | 2026-10-10 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 3488cd81-43fd-3365-80fe-8769939af0f8 | -7.4975 | -55.0055 | 2026-10-10 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 891d1c8e-7822-30d2-9051-216dcdd159a6 | -3.2737 | -54.6826 | 2026-10-10 01:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 31001711-5fb8-3a76-857a-7420f30dd849 | -7.2011 | -52.6272 | 2026-10-10 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 194b2f59-d537-3210-8f86-a229eab9e404 | -12.2324 | -44.6961 | 2026-10-10 01:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 3fe7164d-7372-3e14-9d6e-432e67e13c79 | -7.1825 | -52.6283 | 2026-10-10 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 3d656dde-c3a9-310b-8b89-52afac6f7143 | -12.1015 | -57.1583 | 2026-10-10 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 62cc802b-3eda-3320-b7e0-75ff0f4cac96 | -5.7378 | -45.1307 | 2026-10-10 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| ae85f663-97d1-3b2d-b1e0-9184b263d518 | -14.453 | -43.9598 | 2026-10-10 01:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 114.3 |
| dbaf0a08-e283-3697-b21b-2bf0d351a81f | -6.4566 | -55.5008 | 2026-10-10 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| e242656a-d64d-37fc-af40-608fa97fa708 | -3.5491 | -54.7351 | 2026-10-10 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 97f8baff-87d1-366a-a948-aec6d653f78e | -7.5347 | -45.3233 | 2026-10-10 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 9d3795a1-a2cc-3a0a-951c-cd47ac92b928 | -11.0332 | -45.4246 | 2026-10-10 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| c1f8ecd8-f950-3f2b-a60d-11a6b5957a2c | -7.0225 | -47.6829 | 2026-10-10 01:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 0da43084-2324-3e2b-bdf9-91fd7bc5247a | -7.5159 | -45.3251 | 2026-10-10 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| fa987eb7-ca4f-3ac1-935a-ec1dc0ea8999 | -3.7311 | -60.6018 | 2026-10-10 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 080bded4-9351-32a1-a955-95b430c86454 | -10.6012 | -60.4863 | 2026-10-10 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 241.1 |
| 2e3fb740-af09-3767-a7c2-392900747664 | -9.2976 | -47.3871 | 2026-10-10 01:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 59e926bc-61e0-3ab4-920c-89cba442cc83 | -15.0259 | -46.262 | 2026-10-10 01:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 0a33f00c-06df-31fc-a139-833c3a184e79 | -2.945 | -54.0899 | 2026-10-10 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 03a2452c-1bc9-31be-992a-d1ce8968b92f | -3.9912 | -59.356 | 2026-10-10 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| c36f57f4-56f3-3f83-b089-7297ae584f82 | -7.927 | -54.7384 | 2026-10-10 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| f4ea5dc8-8df3-369a-8558-32c4d62a423f | -3.1284 | -54.1857 | 2026-10-10 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| cb448c5e-824a-3485-8b32-f069c70c7568 | -12.2154 | -57.1287 | 2026-10-10 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 187ff5c4-dacc-3e21-a98e-a9d00e376ad1 | -2.9267 | -54.0702 | 2026-10-10 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 3cdb0ca2-b5cf-3cf9-a648-b1e1e68e8fd3 | -7.5162 | -45.3024 | 2026-10-10 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| eec3483d-2525-3c9b-bddc-b9f8b991b16d | -9.3168 | -47.3629 | 2026-10-10 01:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 7ea1e656-138c-38aa-83f0-7dabe787d8c4 | -3.7494 | -60.6014 | 2026-10-10 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 156.1 |
| 5b18c39b-c87c-3add-b7bd-867109d95d27 | -1.6225 | -54.4348 | 2026-10-10 01:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| d79a2603-74a9-3d6c-8d6e-87ffdab87caa | -7.9272 | -54.7182 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 45d3824f-cff0-33c0-a325-e26794b0a141 | -4.5929 | -55.7168 | 2026-10-10 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| c9a2f58f-4ad6-3640-9f1c-5cbfcad4f432 | -5.7565 | -45.1293 | 2026-10-10 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 7e68bb7c-f76b-32bb-93b1-9b9ad902c9b4 | -12.2329 | -44.6728 | 2026-10-10 01:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 2d42cd59-7e4c-3f39-9874-ac51568564e7 | -3.1114 | -53.7839 | 2026-10-10 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 7eaf6fbe-65eb-3fb9-bfd8-b516a76f23d0 | -3.8391 | -55.7799 | 2026-10-10 01:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| dd6cc5bd-6102-38bc-8eb3-16691aa49159 | -4.4506 | -47.9329 | 2026-10-10 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a9c07009-8e8f-3be5-9901-9640439c711e | -3.8573 | -55.7992 | 2026-10-10 01:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| eccd8b25-30db-3bf6-9363-de910ac013bf | -10.8905 | -44.8232 | 2026-10-10 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 0a689af2-5083-3c44-9e9a-2acf98e83014 | -3.6047 | -54.6136 | 2026-10-10 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 2c182962-4356-3f6d-9ec2-593da8dad5a5 | -3.5676 | -54.6946 | 2026-10-10 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 99873e35-e7ae-38ab-8670-af10b46a97f4 | -7.9084 | -54.7396 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| d96b5b98-f3cf-3ae3-8b0d-417039801361 | -3.5491 | -54.7351 | 2026-10-10 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 477416ff-2a30-3be5-90f9-89b83caaa283 | -12.2324 | -44.6961 | 2026-10-10 01:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| cd5f91b5-bcc3-3b40-91fc-ea2132e09743 | -12.3066 | -63.3701 | 2026-10-10 01:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 9c23de95-5c00-30d8-8aaf-21a7d08f6d8d | -3.2571 | -54.1824 | 2026-10-10 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 72a7d90d-a217-3857-af09-2a394c41c885 | -3.9912 | -59.356 | 2026-10-10 01:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 5426fb09-9fb7-39fc-90b4-83738ca6e496 | -7.0225 | -47.6829 | 2026-10-10 01:10:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ebc84722-0edd-3c15-8f38-05fb7a6a91b5 | -10.6013 | -60.4669 | 2026-10-10 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 792c56f0-6b2f-3b05-8f03-9de1fcf70d5a | -3.2736 | -54.7025 | 2026-10-10 01:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| d65e4f5c-bc35-38fb-ad2f-d7048d81ef25 | -3.5307 | -54.7356 | 2026-10-10 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| cf8679af-d8bb-3a0a-b559-2cb6e7c13403 | -14.453 | -43.9598 | 2026-10-10 01:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| c845141d-d477-3d1e-a6a9-aa546f14fdef | -3.7495 | -60.5824 | 2026-10-10 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 2be2c0b0-7c07-38e1-8d5d-b7ff07eb5512 | -10.6199 | -60.4852 | 2026-10-10 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 9e6f77c1-cfd6-39e7-8c68-d104308cf367 | -13.3666 | -43.8979 | 2026-10-10 01:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| d7997abb-5564-332a-b441-e838e94e70aa | -3.2203 | -49.4417 | 2026-10-10 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 4ef61535-e633-334a-9870-01e1c782fd34 | -3.9911 | -59.3752 | 2026-10-10 01:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 7b418e96-0fc2-33bb-90b0-a12945665660 | -8.707 | -62.3805 | 2026-10-10 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 84ac2860-c686-3e9f-bac2-0433328e0f43 | -12.2877 | -63.3711 | 2026-10-10 01:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 13be391b-6af7-3edf-aff1-de3e0eb0e94d | -7.2188 | -55.0615 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| b07b2a24-5539-366c-852a-8490500253f3 | -3.7311 | -60.6018 | 2026-10-10 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 2226c412-544c-3dc8-be5b-4e53fef90542 | -11.0328 | -45.4475 | 2026-10-10 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 10853e97-10d2-32f3-b63b-0f73b8e106a8 | -15.0259 | -46.262 | 2026-10-10 01:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 74.3 |
| f16cc94c-c34c-31c8-bb24-2f44e6b83479 | -7.1995 | -55.1627 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| ee77870c-c7ff-3d26-bd5d-3202b149aa96 | -7.2187 | -55.0815 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| e9acda2c-0c67-363e-b741-763d994e9c58 | -13.3865 | -43.8708 | 2026-10-10 01:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 2706140a-1adf-3cee-b1df-0d01a167a991 | -10.9174 | -45.5088 | 2026-10-10 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 464a1a30-4f46-3edd-b1eb-8bd09db2e256 | -6.4411 | -55.0424 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2cb493a7-4671-3944-9af0-8441e40b189a | -6.4779 | -55.0806 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 95fed3e8-d7de-3343-b4f6-c6cae860c4d3 | -4.4507 | -47.9112 | 2026-10-10 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 38c3394e-f3fb-32c6-ab31-b248eb9a2f64 | -9.2976 | -47.3871 | 2026-10-10 01:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 490a60dd-b8a4-317b-b20c-59e13cf525b7 | -4.421 | -49.7766 | 2026-10-10 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8361aca5-3075-3c33-8e11-ff93d41d3f27 | -4.5929 | -55.7366 | 2026-10-10 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 63a2587b-1efe-36a7-806e-2000ccf5ac22 | -12.2154 | -57.1287 | 2026-10-10 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 65dd42d8-6fab-3891-afb6-d94c125e0cd9 | -7.927 | -54.7384 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| a7cc4d94-442a-3c26-b8a3-5c7365251c3e | -9.3168 | -47.3629 | 2026-10-10 01:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 31124f68-782b-34ef-afbc-b679fec6631e | -7.5162 | -45.3024 | 2026-10-10 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 9595f95b-da7e-37de-b11b-264f9c67d1c6 | -7.1997 | -55.1427 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| a76f6509-e18d-3af4-a9f7-396c6beb2e40 | -7.535 | -45.3006 | 2026-10-10 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 444647c3-c344-3593-a458-5cf9f2939615 | -13.386 | -43.8945 | 2026-10-10 01:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 5210e209-6ea5-39bd-909d-b74eaaee6b1a | -7.1825 | -52.6283 | 2026-10-10 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 6b075342-f37a-36ac-9e7c-4c0920dd3341 | -7.2374 | -55.0604 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 007dc8f4-6b01-3818-902b-46adda5193e3 | -7.5347 | -45.3233 | 2026-10-10 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 96955ce2-2d0f-3a6a-820a-24e6e4260d1f | -3.6397 | -60.6226 | 2026-10-10 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a888c9f3-e4f3-38a5-a1b3-68542a60e5ba | -3.2737 | -54.6826 | 2026-10-10 01:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 16b0d712-31b7-3a7f-b105-b1c65d5af71e | -11.0332 | -45.4246 | 2026-10-10 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 44e27fea-fe54-33c2-b404-393c64b613f3 | -6.478 | -55.0606 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 41cd0aec-d530-30c5-b1bd-83b0995d4dc4 | -7.4977 | -54.9854 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 1213fb97-577f-38f7-8fb9-054426015f6e | -7.4975 | -55.0055 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 32686cfd-e84d-3ea3-b30c-54ed68a5c01e | -7.2372 | -55.0805 | 2026-10-10 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 1f98c5ef-043c-361e-838e-db5682f78ba8 | -3.7494 | -60.6014 | 2026-10-10 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 3bc5ac80-74ce-32b7-b327-4b171b3ce7f1 | -15.0264 | -46.2389 | 2026-10-10 01:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 29667add-563e-3907-ae95-a35c197244fe | -11.0937 | -44.0975 | 2026-10-10 01:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 279951ec-988c-36f3-b1b5-30d63c646934 | -1.2723 | -55.7494 | 2026-10-10 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| bdcff97b-fd66-3178-88e5-ab6eb1ef916b | -6.4566 | -55.5008 | 2026-10-10 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| bc7bbd9e-340f-3644-ab46-1cac54e51f02 | -9.3165 | -47.3851 | 2026-10-10 01:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| da5fc1df-4394-3999-b36b-1d825fb86064 | -4.4025 | -49.7774 | 2026-10-10 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| e6d8c316-6515-30c4-949b-ea3a934f4694 | -12.2343 | -57.1271 | 2026-10-10 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 7ffef3e0-4c84-3a0c-a157-77425e1c0e63 | -7.0228 | -47.661 | 2026-10-10 01:10:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 5f33297a-ca53-34ad-9442-0b1c54f7feed | -11.0933 | -44.1209 | 2026-10-10 01:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 2d9dfef8-ea5f-31d3-8be0-ca64356ab4f3 | -2.9267 | -54.0702 | 2026-10-10 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |


[Clique aqui para ver as próximas entradas](README16.md)
