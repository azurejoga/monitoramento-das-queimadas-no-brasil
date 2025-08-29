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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2a8355d-61b4-3ea3-880d-8d52d8d5ae20 | -15.01698 | -48.19395 | 2025-08-29 05:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b96be936-0e71-3962-9ccd-fe0e3e7e3d95 | -9.93894 | -46.71112 | 2025-08-29 05:08:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e6495cd-18c0-365f-a8ee-f61a0c972cb0 | -10.98173 | -46.89759 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 21b6f32d-774a-328d-826e-e0f790bb8454 | -14.77799 | -59.73082 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50620593-e421-3bb7-9262-b0cd594eae0b | -10.85711 | -47.49321 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea387ab9-3906-37d5-b6f1-88f69d79d8d6 | -13.18621 | -45.27632 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1703ca24-2913-398c-ad8d-a43975b95239 | -11.38087 | -63.26922 | 2025-08-29 05:08:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97738302-03f5-3146-9834-a06352c25fed | -10.46257 | -57.9376 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6826eda6-02fb-3e51-9f96-5ce0972e5c30 | -13.42475 | -46.97299 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2bcfa702-23ce-3c6e-86fa-e1918db070bf | -13.6611 | -46.90979 | 2025-08-29 05:08:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ea138f9-ab05-3d27-ae2f-9b0702adf924 | -14.78964 | -59.72491 | 2025-08-29 05:08:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5267a405-1f85-36c9-8a55-0b86eab70d5c | -9.11077 | -65.7647 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8c86e8e4-e3d6-36b9-bde4-e04b4fe9377e | -8.95655 | -65.95284 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae6e0d4f-c676-35f1-996d-34b9d58e22cc | -12.68312 | -48.18497 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 592dde74-ecc5-322a-b5d3-963ba9443339 | -13.60405 | -48.16066 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02dc1329-f791-3647-91aa-5646b6600dd2 | -12.99604 | -56.91998 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62a8c5ef-7da5-3cdb-9aee-d3eed269231d | -15.81707 | -48.16334 | 2025-08-29 05:08:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d4c5398-6d74-3c7c-a0d6-e77e8d01060d | -9.93804 | -46.71833 | 2025-08-29 05:08:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e84291c0-4ab9-35fc-bdb8-65d9ad38ca24 | -15.21537 | -53.79545 | 2025-08-29 05:08:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c56ce154-30d8-3c2d-a567-2c39fac7720c | -9.46815 | -60.56115 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09d49519-a25e-3a80-90bf-0b621cf4ff1b | -11.35466 | -43.55795 | 2025-08-29 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66660cf8-3916-3f05-b49d-1a18e2955590 | -10.38276 | -57.83163 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 538a6a6a-5023-3d17-b8b0-fd1c612417d8 | -10.5074 | -64.33411 | 2025-08-29 05:08:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90e9fdb6-1082-30ef-9de5-19d2237c02c7 | -9.23959 | -59.78183 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4af1497-2246-30d1-a03a-baf32b6af44d | -15.54049 | -54.26939 | 2025-08-29 05:08:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60b912ce-adfc-36ec-b01c-972e2f319ee6 | -13.98053 | -46.32833 | 2025-08-29 05:08:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d0056bd-f407-3303-8250-b9020f494cc5 | -13.5772 | -46.86902 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebb4d14b-8fcd-3918-a978-3159b34209f0 | -11.62354 | -47.30981 | 2025-08-29 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46912c80-bf21-37dc-96fd-bba096e554be | -8.18418 | -61.3862 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 13b59450-d655-3b3d-8b6c-2fd31baf1792 | -9.10284 | -65.7426 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7573a416-144b-35d8-b94d-272c2b083fc4 | -12.02336 | -49.71019 | 2025-08-29 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23f8f61f-be49-3900-99fa-0825fb27e336 | -9.0082 | -65.70975 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2977ea78-c3d3-3eb5-ab2f-705fc9eb1660 | -10.49807 | -51.6154 | 2025-08-29 05:08:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9921707e-20e7-3887-b8c9-6d225cc2b942 | -8.95358 | -65.97097 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1da40bc6-87df-3592-92d7-434990ec13a1 | -9.10862 | -65.77247 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| fe89b882-4bc4-3e2c-8940-931e338e421d | -13.55124 | -46.94153 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5173b28-7ac3-3132-ba78-bcbfb59ced2b | -9.16082 | -59.53688 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb1fe566-5996-39cc-8f0b-2042633aa87c | -13.41791 | -46.97046 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fe0e3b20-bb79-34a6-8f2b-6b5814faf14b | -10.3458 | -59.18919 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2119b950-acc3-3c1a-b30f-f9409db4ed35 | -11.70257 | -60.19487 | 2025-08-29 05:08:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b96d7ca3-eabc-3c3f-acd6-c0a94bc8fe83 | -9.80434 | -67.84235 | 2025-08-29 05:08:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2795cd26-d9e3-3a8d-9bfc-4196a64d25e5 | -9.93987 | -46.70362 | 2025-08-29 05:08:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56851db5-5944-3b90-bdfe-32134f4e6ea1 | -15.19311 | -52.34147 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc72cb6b-1a2f-390c-8dcc-75e7a93642ae | -14.601 | -54.5005 | 2025-08-29 05:08:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee0f8675-ab84-3aa0-aa38-10e8259c3305 | -9.21545 | -60.87247 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6604a4de-86bc-39ed-ae48-617224077a20 | -13.62045 | -48.24901 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 154e0e88-5d6e-34c8-90bb-f1d18032715f | -10.45686 | -57.95153 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cde13084-d039-303d-9661-ccf81e50e7a6 | -9.94154 | -46.70697 | 2025-08-29 05:08:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e96b10a-e6b4-3a4d-969d-a5d8de78baee | -14.30484 | -53.29712 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5790f37-3364-37e4-aa6e-ef3863bcd6a0 | -13.54054 | -46.88144 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0f96dece-7139-3b08-9451-762dc8199e19 | -11.56845 | -46.37614 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94e04ca2-31a1-3ee9-86df-d629f6c84109 | -12.85855 | -48.10036 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d741dad-3d4c-3038-9196-1d0088179909 | -13.42325 | -46.97449 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 26c1ec27-1386-3d65-8d6f-d1e3a8ef3abb | -9.6077 | -55.37835 | 2025-08-29 05:08:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7800ab6-38a4-3fe0-8a0c-06ef854f0631 | -13.45591 | -46.95557 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 335e6294-c333-3190-aebd-124c78db671f | -13.00825 | -56.90741 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2ec0e75-0088-35b0-b800-c23f7cdb498b | -13.19838 | -45.28308 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f001fb01-4854-3fbb-8fb0-1df4eb87afa1 | -10.98132 | -46.91806 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2b00e9e3-897e-309d-bd4f-df5b47cf5620 | -10.6978 | -47.07677 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e29676cf-b1a6-3382-bc4a-4c340322eb7d | -8.10929 | -61.21929 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e02f5618-6ace-3e7c-812b-c55ce771d4a7 | -9.44905 | -60.55764 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 735361e9-d642-3e9c-a329-f9b9284775d1 | -9.17561 | -59.44854 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dfd1aebe-d304-3830-9ab0-e19f73cf2a57 | -10.45861 | -57.94066 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02a25f3c-c3aa-3144-816d-db474c7cdb74 | -9.77608 | -64.25797 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 3d57b3c0-7f7b-33ce-8c35-96d7fde51f05 | -9.10798 | -65.77599 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d3c100b0-23c4-33bc-8fc1-11716cc73477 | -8.95424 | -65.96738 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2851ae3c-e6ee-39fc-9e1e-e5fc8dcc5ed0 | -15.01656 | -48.1976 | 2025-08-29 05:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d034093-88c4-3dc2-be48-91dad32162b5 | -10.46316 | -57.93398 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3296be8b-015f-3ae1-900c-db745ffb5064 | -10.02369 | -51.10551 | 2025-08-29 05:08:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9687bf62-5709-3864-aec8-a093147fb938 | -10.45463 | -59.12131 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d708b16-4b66-355e-8f49-bfb98f9ca61e | -9.80322 | -67.84376 | 2025-08-29 05:08:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9b01d362-5af7-3a9d-99a3-ecb838682ec8 | -11.26752 | -45.49496 | 2025-08-29 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77853c63-0d0a-384d-abfe-cbbfb7a8c061 | -11.55893 | -46.35744 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b9a4e3e-69b4-38fb-8aa1-8e126a3bc760 | -9.16171 | -65.79227 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08c6f42b-8e44-3738-8577-96affb29cdf2 | -9.10958 | -65.79814 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15e5ed2c-e7fe-35c5-9911-4c08d6c2f0bb | -13.54141 | -46.87377 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f83ea8d7-d46a-39f7-ad82-71b609629139 | -13.40649 | -46.96855 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 281eb695-60a3-319f-a898-5302f57f2dcb | -9.54691 | -65.69611 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a2c9a0b-c66e-3d5e-b3a4-d6058fbeee7f | -8.30171 | -61.40639 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e872010d-679b-3f3d-a56d-a9527dba93ac | -9.67284 | -48.32448 | 2025-08-29 05:08:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52c279f8-7fed-3b8b-a739-59bb959d30a3 | -12.83112 | -48.10468 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e7a315a-ae98-350d-a1f2-e5536edcd9f4 | -12.83418 | -48.16138 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df8a46e2-a686-3c55-a541-ec796715dc0f | -14.29912 | -53.29356 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7019c523-bdcf-3747-a44f-5860a53bac8e | -10.46406 | -57.97147 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8558255-2342-39a5-8e28-37c5281c6a99 | -9.16385 | -59.56339 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02c88c11-0c5a-398a-98a4-0cc8993afe07 | -12.61954 | -57.01094 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2b210e3-8884-351d-8622-62698c3fb298 | -11.51277 | -57.99045 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2af74903-1873-3a8d-80b2-555c5b4b0e80 | -9.13528 | -65.29412 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b73fc852-18e9-38fb-a44d-71cf1833726e | -10.87722 | -56.36925 | 2025-08-29 05:08:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 94f68c87-ca55-3bac-aac7-1c0b1a51dfd7 | -9.10949 | -65.77151 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 23927a99-67ce-3335-9264-590fcc054dc2 | -12.99993 | -56.91697 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb6f7665-898e-323f-a5d3-a8f90f66ccb2 | -11.8777 | -46.39787 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 93fdf569-1598-3a7d-b6d3-6ff5ae7f4e61 | -14.31498 | -51.89489 | 2025-08-29 05:08:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 536dace8-2542-3186-8958-22776159f0f1 | -12.8307 | -48.10798 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7272b6b4-2db4-385e-a0e4-cdf86733d13f | -13.68497 | -46.9063 | 2025-08-29 05:08:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e94dfea7-c809-32ff-be4a-12bb72a5cbd5 | -15.6691 | -52.75085 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04c06d68-2192-3298-ba0b-7141825c24d7 | -13.18564 | -45.28154 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f872ad50-fcb7-3469-8904-4175f9a94311 | -9.12312 | -65.78854 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd0fbd5b-2b28-3114-a7bc-8ac2354b7c24 | -10.45349 | -57.95097 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06b4cf7b-9989-368e-a69b-120e427f2c12 | -12.68833 | -48.18602 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README66.md)
