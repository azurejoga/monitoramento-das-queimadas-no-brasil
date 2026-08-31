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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc1ff745-b7d9-3233-939d-605177e204b3 | -4.30536 | -49.0999 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 1032b332-620a-3630-8079-ad1cd5c44aff | -3.003 | -42.93454 | 2026-08-31 16:52:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a9ea8be4-c7b4-36d6-b789-ee8e7224ae75 | -3.11819 | -61.22784 | 2026-08-31 16:52:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8008ae21-5b05-3b3e-bb85-ba6367dd7225 | -6.24931 | -53.67894 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| fcc5993b-a273-34fd-b450-f235d98167ba | -6.08814 | -57.71953 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2e197985-3cde-305a-b27e-d854663a92da | -6.82145 | -59.67786 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 30e03ec4-fed7-371a-a7f3-860c3e228d20 | -5.85907 | -57.55185 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5ff0c765-5b77-37a2-b057-988f5c6208c2 | -1.1886 | -46.947 | 2026-08-31 16:52:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 45df8ea4-bbf7-3502-b60a-fa67fd0b7828 | -7.30628 | -60.5701 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| da02bc1f-ef9e-3415-a6e0-c04cc5f3105e | -3.6495 | -54.85095 | 2026-08-31 16:52:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8b18f056-432e-3d9e-9d2b-ca935d7020b6 | -5.95963 | -57.67934 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ab5b5bfc-b47c-3d14-9a22-0c7d0ac2d368 | -5.45818 | -60.23424 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| e935fabb-aa14-38d6-b4a3-f96e92f17bce | -7.33672 | -60.58858 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| de871888-7569-3fb6-ad7e-0264ec210c80 | -7.30945 | -60.57597 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 2975cbce-7255-3299-87c1-00d4c0c4214f | -5.45621 | -60.23745 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1f39a89f-dd5e-37b1-97d5-962e802511a7 | -6.87011 | -59.46606 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bfc44e7e-ff98-3819-974a-f3b3ad521993 | -6.78167 | -59.78721 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 8c2cc4c8-7846-3b26-b118-02c21812d3e1 | -6.10837 | -55.82011 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| dea856fa-0a41-3f3f-bfeb-1e227f40172d | 0.19221 | -60.50063 | 2026-08-31 16:52:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 54921739-fead-3153-85d1-9388ee814000 | -5.28027 | -47.88773 | 2026-08-31 16:52:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| fdf49c89-c2c1-3220-90ef-d0ceefe46520 | -6.25335 | -53.67575 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 08b0cd6e-46a7-3a2f-9edc-a45f904cb927 | -6.99266 | -60.68079 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3b552f09-d0e2-3302-beba-2921b99a6abd | -1.80163 | -44.8527 | 2026-08-31 16:52:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 4a36010b-8a39-38a9-b130-e66428d0baca | -5.88019 | -57.78185 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa172367-43a5-314a-accb-3c6b35e04749 | -5.96746 | -57.67543 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 217e7f97-9987-37c4-9b07-137ba0f9b081 | -3.48574 | -54.66472 | 2026-08-31 16:52:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4d49d56b-76ac-3569-b7b7-af812050b888 | -2.4359 | -48.43469 | 2026-08-31 16:52:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 20561f5a-12d6-346e-bc09-b6d9c72a5fc3 | -1.69387 | -48.25313 | 2026-08-31 16:52:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 7b9abab3-393d-3eba-8698-d3266a562321 | -3.32007 | -49.86996 | 2026-08-31 16:52:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5c88c0a6-4e2c-39e9-b7ad-a03e971cda81 | -3.61319 | -59.07073 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| c1097206-65b9-3d4d-b863-3c6e446c97e0 | -5.24278 | -55.88982 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2bd3bf47-ffcb-35c3-9607-3307535622e1 | -7.3347 | -60.59266 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| b39e4576-6f6d-3d80-88cf-2a79d1ba45fc | -3.40892 | -43.37671 | 2026-08-31 16:52:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 5033cdd9-57f4-3f17-882c-18beb3ccbd4e | -5.86477 | -52.09036 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7c333501-6212-34a3-8404-4d60fa7b714c | -5.94519 | -57.68742 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 06c15dcc-115d-3086-9e57-fce9140fc6fc | -3.82633 | -56.94514 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c2671d8f-ceec-3cb6-90a7-c863297e0763 | -4.42531 | -55.4328 | 2026-08-31 16:52:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bb2d75ab-dadc-3df2-a584-4bda0ebdd5a1 | -2.797 | -43.49355 | 2026-08-31 16:52:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 8fcf03fe-301b-3c92-a0ee-2d11ce8bc42b | -6.59761 | -58.60226 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a927ce66-1e89-3d2b-8c37-88ebe2f4228f | -4.07106 | -55.77791 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ac988db6-3ae5-324d-9a7b-545dad260cda | -3.20998 | -61.16933 | 2026-08-31 16:52:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fba6bccc-3077-30e7-9ab0-fed1c5868ef7 | -6.85152 | -56.39295 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 90fbd5a5-9777-345c-8eef-aa28d7745df0 | -3.45757 | -60.26578 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aaf9b041-d46c-365e-a5de-326f20858b13 | -6.72427 | -58.7042 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 27effc5a-52d1-35b4-946c-9b699b7aa320 | -1.31706 | -46.34804 | 2026-08-31 16:52:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0cce63a4-019c-3d08-9331-c47a041650a4 | -6.65842 | -59.43284 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9713faef-4fb5-33c7-946a-f5c96302dca5 | -7.48286 | -61.38922 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ab620a29-647c-39b1-a2f5-5c74af1147e3 | -6.26051 | -53.64712 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 2d72ee74-db96-31f7-ac6e-d98b6e7434b3 | -3.31954 | -49.86652 | 2026-08-31 16:52:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 6245ee0f-d2dd-3992-8aa1-95b0888e2ae9 | -1.94495 | -50.64723 | 2026-08-31 16:52:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| d7323efb-c371-3df3-a9b7-ca0501424b94 | -4.97127 | -55.84639 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 16f2a4f1-bcfb-36a4-8c54-d9e4d65988f2 | -1.21423 | -46.6063 | 2026-08-31 16:52:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 3dafdf64-f984-3d9b-89a4-b96a628f24d5 | -1.04298 | -48.18815 | 2026-08-31 16:52:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3dde88f8-c667-34c1-b89f-56de2b5ee2f4 | -6.86545 | -59.47519 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ee8a6920-2ada-3757-a223-57da95d819ae | -3.38832 | -59.38838 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cd382ab5-d440-30d8-90b4-e7428af8f229 | -6.80368 | -59.77088 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e85025f5-a62f-3ea7-b66b-efe89ab41c98 | -3.2651 | -58.23572 | 2026-08-31 16:52:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| da866717-cc73-3b08-a453-25ef462c1b6d | -6.25248 | -53.67347 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| e77449ba-45bb-3d9b-acad-61cdc24b9488 | -5.98097 | -51.92329 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4cddc2d4-f621-3b5e-9272-de89d6df5ce5 | -2.48347 | -49.06081 | 2026-08-31 16:52:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7ae0983c-6743-39e1-9632-720ec4845cbe | -1.93594 | -44.80432 | 2026-08-31 16:52:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 666281ae-b86e-36c7-864c-d4f641678368 | -6.37104 | -55.21601 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 178aa275-34f5-38b9-a777-aa99d35524ca | -3.79912 | -59.34699 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b12beeb7-b602-373c-ae3e-d3f860e5e2cb | -6.4138 | -54.76447 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 378ee806-9dfc-34a8-a04d-e7e477ca105e | -5.8918 | -57.75237 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f91bfc0c-39eb-3ea4-8e70-5327ce4d8789 | -6.27828 | -53.32831 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bb69919a-d515-342e-a9af-39ca9762125d | -2.88747 | -41.79567 | 2026-08-31 16:52:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 06155589-e176-3bd2-8f3b-c94d7010ef48 | -6.32065 | -54.74609 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| da804c16-9cbb-39e1-b449-d5d3b59b8055 | -3.40584 | -43.27361 | 2026-08-31 16:52:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e9584644-dcf7-35d9-920d-d8ef09975f5a | -6.27752 | -53.37654 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 743951b8-0e23-39c2-a80f-314e5c9d89c1 | -3.29606 | -58.00069 | 2026-08-31 16:52:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 49c5d4a9-dfb0-3931-980f-51fc1a5b6012 | -4.96375 | -55.85437 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| dce90b36-3507-366e-92eb-c9f1ae87237f | -3.87404 | -59.56219 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7633519e-e140-3cf1-91ab-ad975ddc5ffb | -2.67079 | -59.37024 | 2026-08-31 16:52:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 39d3e6d2-0f31-34ca-87da-16f38921c1cc | -4.59607 | -42.92346 | 2026-08-31 16:52:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| d641aec1-2f04-3737-9f59-f95775198195 | -6.25655 | -53.67025 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 35df8b05-7f51-32c8-94d7-1e1ce6424a89 | -1.59392 | -54.40024 | 2026-08-31 16:52:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8a6a3d5a-9d8e-32ba-a39d-4793ac410141 | -6.05624 | -57.64208 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 17d10b65-5ba3-382d-8443-fb6290ab7ea0 | -6.85997 | -59.4811 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 31dd99a1-260a-3be0-aae5-6ef0c7278898 | -6.5981 | -58.60578 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cee0865e-d942-345e-8007-bfe3053c7dcb | -2.04043 | -48.22963 | 2026-08-31 16:52:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a5f894bb-a11b-35f2-9fc2-4d18ab443fb1 | -5.89528 | -52.24749 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 57b4c9f7-42a8-32e6-a8c9-e218fd4819ed | -3.47841 | -45.70397 | 2026-08-31 16:52:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e4353431-0c19-393d-81be-db52c0824380 | -6.8057 | -59.77075 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 36bc4e53-11a3-3921-8bfa-fbbd14316672 | -3.69636 | -47.7914 | 2026-08-31 16:52:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62b045a3-5a04-3d9c-9b47-04e99c038a7e | -1.45751 | -54.21899 | 2026-08-31 16:52:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| bfafc345-4775-339e-b8b0-8e0f139ea0d4 | -2.48948 | -44.88075 | 2026-08-31 16:52:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 54e15a3c-8149-3a23-b421-8e7ed4aaa601 | -3.65021 | -45.36879 | 2026-08-31 16:52:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9c4b68e4-7ed0-3fb5-bf2c-3da3cd8e7136 | -5.97089 | -53.5792 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 692b128a-b913-3350-96ef-627a6ee64c42 | -6.86436 | -56.4167 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3298d3ba-3115-306a-8e6d-1901ffb327a0 | -0.96984 | -47.37846 | 2026-08-31 16:52:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 10301781-f810-314d-aafd-52d6c9ba5780 | -3.32615 | -49.86553 | 2026-08-31 16:52:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 1b59e0ad-0f36-3dbd-a148-411f4e0bc893 | -4.49631 | -49.34959 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7eadb68e-37da-357d-b3d0-2b3768d9c9d9 | -3.39117 | -59.36963 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7e51b7cc-e50b-32c2-9a7d-54d7a68307d6 | -4.30045 | -49.09002 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| c089b738-fc16-3e75-819a-29996766dfdb | -6.13208 | -57.6764 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b10859a9-470b-3acd-9d10-fb256eb57ceb | -6.17992 | -55.44567 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5ec4b990-a80b-3d6a-8aa9-9e991dc7e863 | -4.21297 | -48.6109 | 2026-08-31 16:52:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 83b0a03a-399a-3332-8d40-59bce6a3d6f5 | -5.49111 | -57.14712 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0c7b8da2-4f8d-37d5-bcfb-8915d98c5f93 | -2.67129 | -59.37371 | 2026-08-31 16:52:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |


[Clique aqui para ver as próximas entradas](README168.md)
