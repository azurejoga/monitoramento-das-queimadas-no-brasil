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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1cd1cf4-05ba-3459-a77f-476e9c71475a | -14.28425 | -51.78627 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7950f707-1549-3b51-a9bb-297f87714ac9 | -19.00063 | -44.70254 | 2026-08-24 04:46:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbd46e12-130c-3b30-8e96-92a9ac395a64 | -12.09781 | -50.60081 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 7338ff8a-d5f5-347c-b6a7-e74718d1688f | -10.29407 | -48.20077 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90d6ef72-5946-3d39-a014-7d9cfb5fa337 | -9.03011 | -50.71141 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48453a12-ab59-3311-94b1-cdb6d4ad027e | -8.58679 | -49.99409 | 2026-08-24 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aedd4898-da80-3a90-a666-1f332c3b08d8 | -9.05763 | -50.77322 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c20e75cd-69cf-37b3-bc47-b413899c2609 | -14.33619 | -51.75867 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 791fbba3-8b91-3771-b572-aefe11a1098e | -12.74758 | -46.45556 | 2026-08-24 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c77ae838-8db9-32ba-9b21-dc9aaabcec21 | -11.84834 | -51.67752 | 2026-08-24 04:46:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db8b22cb-9a50-359c-a60a-398d9cb7e061 | -9.96718 | -48.32894 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6eefe5a-8603-3c86-bd4c-18ad9f780be5 | -8.31205 | -47.58562 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65b82ea8-cc6e-36d2-88aa-0f705e9f9bda | -12.1072 | -50.62764 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40486e84-cf3d-306d-9cc6-e9d9b453346a | -6.8055 | -58.66614 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 076ac731-dced-390e-ae26-ded0b5d3ee10 | -12.11825 | -50.60051 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c7612361-341d-3c34-a4ce-f0fda32bfa88 | -10.79592 | -50.95145 | 2026-08-24 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8f684b9-3c0b-3daa-9ab3-b455e16a2507 | -10.45967 | -46.22262 | 2026-08-24 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d802379c-3308-30d5-ab07-83213977b52e | -11.41455 | -45.12315 | 2026-08-24 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88ce2098-abb9-39f7-bade-a17c91fbca59 | -6.8966 | -55.6983 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 058ed851-acd0-325e-90cb-030eebb64bcf | -14.77922 | -48.78386 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73382be6-0757-3de7-b04d-54f4439585b0 | -10.69763 | -47.74327 | 2026-08-24 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5eab8719-cf77-3e47-b76e-5eac8cd998bd | -14.44464 | -51.80228 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78aeeca5-5d72-3390-a421-63187a8c0272 | -12.09891 | -50.61545 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed098bba-55cf-3b79-8e18-c6e117d417dd | -8.58955 | -49.99809 | 2026-08-24 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 557d74bb-71ab-3b68-a5aa-338511f2d1b0 | -14.78748 | -48.7768 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a59af3e-a489-39ae-866e-a95b2f7b6589 | -8.30224 | -46.88795 | 2026-08-24 04:46:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3764684-0255-314f-8f8d-0393b9372014 | -9.09716 | -60.91014 | 2026-08-24 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41e81db1-8054-33c3-b8c1-3daddfa3cb5a | -9.39158 | -60.58862 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db663a43-8dee-3bfd-ad2f-d301a281f8ff | -12.89472 | -48.46589 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4fab2679-a346-3d21-96f9-d4a10426f27e | -9.94933 | -48.33039 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90a46810-703a-3329-8eb4-c8797cb12f31 | -6.38665 | -57.4689 | 2026-08-24 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16f21c9b-e338-3715-afba-4c37bb15572f | -12.71971 | -48.40359 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1324579b-ca9b-35ca-808f-c720e44639cb | -12.81978 | -48.48261 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 319642a8-b8ab-3ee8-a211-7eea2e1425d8 | -10.69407 | -47.74277 | 2026-08-24 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d758cdfc-ba0e-3eff-bd23-98e1b14d8fdc | -9.17346 | -58.07285 | 2026-08-24 04:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2501d70c-b1d7-300c-a329-4e289460834e | -9.03003 | -50.75441 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ddb4d004-67f2-3eb2-9ae8-b3715784560b | -9.05045 | -50.77563 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 280c54a5-b80a-3686-a13c-9a1ea4837b78 | -12.35092 | -51.21262 | 2026-08-24 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c9468ea3-5c24-32d1-aa22-95927b124fd3 | -14.33288 | -51.75811 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 072c8f4c-1a73-3ae9-91bc-086879068209 | -13.27768 | -51.43032 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acaa20a5-3b61-3d5e-b7cf-ee4440e9b395 | -8.09552 | -50.05096 | 2026-08-24 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d20919f-d4ee-3996-8583-eedc1a8cefca | -8.81078 | -46.61102 | 2026-08-24 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f6f2ec5-547e-394e-8f55-cb09b22fc1be | -18.53204 | -47.17295 | 2026-08-24 04:46:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2868c93-6484-3acd-9ad5-1d97af6fa7a5 | -12.0862 | -50.58818 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d248ba0e-df70-39ab-bef5-35978b51d43a | -12.09449 | -50.62196 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76af8ca4-f9c6-3065-bd20-58bb6db4e31b | -14.34318 | -52.9501 | 2026-08-24 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65be9356-43b8-3898-9bf7-ebb1a6e5c8d3 | -12.11438 | -50.6035 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3a29669-bb8c-33f9-90ee-21055ef54d9c | -6.54974 | -58.52582 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 300b2c52-3e9e-3e28-bf92-5f5b2a23707e | -8.38365 | -46.46866 | 2026-08-24 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92b93cc7-bac5-3b77-9473-93b7e3525512 | -9.682 | -47.89629 | 2026-08-24 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dbeb511b-33a2-32d8-ac59-caf7ee4d76e8 | -10.80366 | -50.94552 | 2026-08-24 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85b6ce6c-bc72-337e-a6ea-3423f6e5d187 | -8.09549 | -47.4832 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 618a5a50-8dc2-3160-bc95-f809c35cfc7a | -6.81406 | -58.6493 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d644e252-4f93-37e4-9991-2fb8df329d17 | -12.10996 | -50.6317 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5a66c64a-de16-370b-9f67-78888835f7fc | -10.69584 | -47.75542 | 2026-08-24 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdf634c9-bc6b-3c53-a677-4ce522c0b3fd | -12.11493 | -50.59998 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 644f56c0-cf4f-33c3-a959-9126c24529d0 | -8.81447 | -46.61156 | 2026-08-24 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd146dd4-c3e5-3f5a-9ff0-85b91d174c68 | -10.27404 | -50.38618 | 2026-08-24 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 695e1c85-b238-35dd-8d22-f80dec2ff50b | -9.95278 | -48.33086 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5003084-5f23-36dc-b636-9b7a18ee960a | -10.46702 | -49.5216 | 2026-08-24 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0a8a413-a5a3-3384-949e-c317d1e67ceb | -12.11549 | -50.61814 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 666e5885-5e00-331d-8e0b-8dcac7ca26b9 | -14.77687 | -48.77512 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 52feb93e-2540-3f0e-91bc-7c1bc6b76a4f | -11.67076 | -54.5461 | 2026-08-24 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1111979d-d2b3-3411-8e74-0427bff9b4fc | -14.28687 | -51.79055 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccd9e58c-257b-38b0-80b1-e8cf189c63bc | -6.89234 | -55.69749 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7267487-3014-3cce-8642-579ac9f883dd | -6.55413 | -58.59227 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f648ffd-1df7-333a-b778-ad6c650b544d | -10.7287 | -47.97173 | 2026-08-24 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b2d9992-3e6f-33cf-98a2-f38f0658136c | -8.10599 | -47.48489 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe98457a-f6cc-39fa-aa1b-bcdd2abb4ea9 | -8.08891 | -50.04991 | 2026-08-24 04:46:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2d24ed1-bdb9-39a0-9ef8-612888033cea | -12.0613 | -50.57368 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b95b2778-2825-3d04-baf0-1b25b34e9a77 | -13.55317 | -49.09143 | 2026-08-24 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e696a04-ee26-3537-8b06-22c9a3d3f6a0 | -9.87026 | -60.10381 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f29ef3c6-4feb-39ca-a369-ce906a7ddf57 | -12.12046 | -50.6081 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 40d7a65d-a827-39d3-b162-91896d3d9dd0 | -8.09899 | -47.48376 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3aa76c66-3cf3-39d4-8369-91b29f16b1a0 | -12.25307 | -43.11488 | 2026-08-24 04:46:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d8583aec-392b-332a-98a4-f18361c3039a | -10.29698 | -48.2051 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26e8d075-fb56-3303-821e-cf10e726521c | -12.21576 | -43.17417 | 2026-08-24 04:46:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4bd44c01-8960-3902-a5ad-aa071cdba805 | -11.38895 | -50.72421 | 2026-08-24 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c04a4c4a-8585-33f5-891e-eaa05704ebf6 | -6.78427 | -59.65766 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8621376b-6783-3a99-a6c3-a3bfe8effc66 | -9.51087 | -60.49919 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70221821-2c8c-31f2-98bc-3d9af0ddb112 | -12.11052 | -50.60649 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efebed3a-c213-392d-ab06-8ff69da2659a | -13.89862 | -54.04095 | 2026-08-24 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46f283f4-3f68-3ff8-a138-8259d4b50df2 | -13.4306 | -51.81227 | 2026-08-24 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8b69c1d-6e31-36dc-b9b5-5e8689012d2c | -10.46173 | -46.22016 | 2026-08-24 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fecee5ac-caad-3fc7-82cb-6a6924afdb74 | -12.10277 | -50.59086 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15761ab8-40f7-38bc-bc89-a25d5c84c512 | -9.47019 | -56.92199 | 2026-08-24 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd551f88-e3ca-3b24-be13-954d151cac9c | -13.65347 | -51.86358 | 2026-08-24 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c33a8f67-758e-32bd-8c05-aec9076bc133 | -14.77269 | -48.77897 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0d602fd7-2c56-3925-b526-b16cd61a0852 | -7.79068 | -56.29031 | 2026-08-24 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e260c2fb-9865-3e54-9392-f90651eccc87 | -9.8696 | -60.10735 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aea2e4e4-ca5c-3e5f-b386-6dd5141e5164 | -11.86269 | -51.6945 | 2026-08-24 04:46:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bf47b3b-5a6f-366f-a00a-ac61e88c6e53 | -14.329 | -51.76111 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95a7ff9d-f117-3a57-af60-55447535fccb | -11.20303 | -55.04956 | 2026-08-24 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 695d03d1-0526-3a58-8a75-51ed711bf9c0 | -8.57682 | -55.27833 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94b31344-fff3-340f-9698-729ed21aa837 | -12.10333 | -50.60894 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 60c54254-9207-34c4-9e0b-42af3c81ec77 | -9.68168 | -48.3681 | 2026-08-24 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f15c600-6a8e-3e22-a106-5aa37f0017a3 | -11.98752 | -45.50457 | 2026-08-24 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25c7ccaf-a005-339c-b077-efe96f78d460 | -14.35938 | -51.76256 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1e1a409-8691-3998-adf2-ea6e8671b7e4 | -12.10886 | -50.61706 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35b0c196-c56b-380f-ba18-e1af8947d413 | -10.81635 | -50.95118 | 2026-08-24 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README34.md)
