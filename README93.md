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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30cf83c7-8e4f-336a-9c16-387f1cb8aab2 | -10.74282 | -50.78419 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77ab7dd8-2a40-3224-84c3-e4aef2f1e3e8 | -9.56047 | -66.05891 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fadcb6f1-fdbc-335d-bd61-8b0640b0015f | -11.10486 | -51.05861 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aa203633-5e96-39ed-97f4-ee58a9a425d5 | -9.7421 | -65.01878 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c94d2e1-b355-30ae-9f89-77d90b4b08b1 | -10.42843 | -50.24391 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e0e8009d-541e-30cc-be3b-a86c07dc5463 | -5.92729 | -59.95335 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3e051ac-be0d-3c40-b078-8e9cfd94df7c | -5.83636 | -53.51629 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3b1e931-78af-3aa4-9dbd-6e493ea8b2ea | -6.41686 | -55.01232 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68055df3-54c9-3ad1-a00a-0e353fb2b78a | -7.32777 | -55.21932 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f34f250-899c-3690-b740-1b8c769f9ee6 | -9.55798 | -66.00644 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3379b65a-3390-34c5-bfc9-5e926ce64f93 | -8.6098 | -54.62547 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1d77397-6183-30ff-9902-b9cb8343b707 | -6.69218 | -60.01249 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2477bebb-152e-3fac-8d76-574291a88357 | -9.55239 | -66.04015 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be5e6c53-7aba-3ac0-80c0-d744d6b264f7 | -6.14439 | -59.94729 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df3f6331-53e9-32bc-8d6e-a10f51d28980 | -7.24389 | -55.606 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6eaa269e-2661-36f7-8b75-568e2e7bd660 | -6.82836 | -55.54514 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0361c294-c7ef-3f37-8b52-c73638949011 | -5.83602 | -53.48206 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecaab8b8-b734-37d7-b4f9-568b5282cd1c | -10.88133 | -54.07104 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 300139ef-534d-303e-bcc8-e0fb9acd6f25 | -6.1924 | -57.77362 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ed775f3-d6e7-338b-ae1e-413440bbaca7 | -9.55379 | -66.03171 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88c0714a-57de-3867-9b4d-5e63f2426aba | -6.30864 | -60.01812 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9dafb8c8-6eb5-3ef1-b4ce-c7aa376d0bd5 | -6.43579 | -59.97405 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e55b8615-0eac-34af-891d-647d5b071ae2 | -7.12905 | -59.65025 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4020bb26-1251-34d3-b7d9-c1cd236388fa | -6.29736 | -59.93096 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9991cfa0-0fc2-3963-bcf9-fe215da28bbb | -8.91025 | -62.37363 | 2026-09-21 05:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff15a030-c7c2-3ade-876b-f8e3972b61ec | -5.84223 | -53.54815 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49939dfc-0546-37f4-8a20-5fb2c2aaf961 | -8.19273 | -54.70229 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b89b4810-f51f-307a-bacb-f8d451a004d3 | -10.9193 | -53.94646 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f836856-ce00-3559-afa2-48250afe0e36 | -10.80877 | -50.83788 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6c594aa-78d3-34a7-81d4-30649054606f | -6.14613 | -59.93594 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c9e55b9-c40b-3a9d-bf6e-cdecdc6b83b6 | -11.03553 | -54.14759 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c514a895-a365-30d6-bbec-c98b819664b5 | -10.81043 | -50.7757 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5af4f4cc-5f57-33e6-bcec-6c8d1c0f7392 | -6.72744 | -55.08948 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5848c9b9-b8d9-3387-a888-0d9b33cafd3e | -11.0449 | -54.15878 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cef10d7-6aa1-3836-9493-2a351f911792 | -6.45833 | -59.98931 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2b499d11-eaf5-3795-9d55-f662d14e622f | -8.61377 | -54.59073 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 233f9e07-aec0-36c3-9b30-eb4611c09b69 | -5.88012 | -51.58603 | 2026-09-21 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48a2048b-d2d8-33bf-9af5-e7423a53766f | -6.33901 | -59.94841 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34335804-075c-3f01-9df6-c77e2c921817 | -8.0859 | -55.34132 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94af3eb3-d7ba-3bcd-82d5-42d1a78c117d | -11.11248 | -54.01206 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa3f4d25-f786-334e-b621-6dc98cb257de | -10.47266 | -50.27366 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ef538424-a710-39b5-b169-e8ba78a8acb6 | -9.55461 | -66.04919 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2aace0c9-529a-3f48-ae74-e47cef716de1 | -5.85 | -53.5307 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd02fc0a-d293-3e5d-9a71-bd7ca167ac79 | -5.41937 | -60.21607 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ba43988-ec14-3cb4-ab8c-de88ce82e2d2 | -11.01594 | -54.13158 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b54118e-6129-36fb-96c0-7b7a98869ab6 | -6.44967 | -59.97623 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 583bec65-f15d-3395-a861-352f228aa06a | -9.03644 | -61.65526 | 2026-09-21 05:42:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e737d060-428f-3ac2-a9d9-0e7dd9ffda23 | -5.80664 | -57.74368 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e159c443-df1b-347b-bd17-e010b8476320 | -8.17748 | -54.77762 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec5bda2e-29d5-36e3-91f8-1b803048f6bf | -5.97325 | -55.3653 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 644f76c6-4bcf-3eb9-aef6-9d565db9cb6d | -6.20952 | -53.56372 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a78a8e9-0a9b-3f94-8a57-d26c418acced | -5.88841 | -53.64129 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1a12c85-ef3c-3351-b71e-db9eccdd56fd | -5.20268 | -56.10855 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9eb71794-bdc5-34e4-8b0a-1a6a3da848e1 | -8.9578 | -64.40624 | 2026-09-21 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f0313eb-6968-340f-8a06-20e289e12144 | -7.25296 | -55.60737 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 983d2dc9-d52a-3564-b753-20e59a647e91 | -6.44914 | -48.44569 | 2026-09-21 05:42:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7c9a0fc-b3c1-3fdb-bec2-df04316bdebc | -9.93614 | -60.72535 | 2026-09-21 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ec4c1fb-1764-31cf-9724-09ba8b398c02 | -10.79031 | -50.76778 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2dd2774f-bf44-3a7a-b30b-35a19a716949 | -9.56912 | -66.05171 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b28b3bab-0fd0-3175-b4e3-7437df8bef28 | -8.05016 | -61.33015 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 577903a4-a3a1-3c7b-af66-bccc2c1bd7e6 | -6.09457 | -57.6831 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d03af3c-269d-3bf7-977c-ebd295b9abcb | -10.9229 | -53.96063 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa092133-0b6c-3932-9f6e-8379c7df9520 | -7.24909 | -55.60207 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a413ddf-bf49-3edc-9b7b-69a83c5afbdb | -10.80455 | -50.7693 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3f1dde10-d66c-304f-93a8-8af5f25466aa | -11.02795 | -57.24629 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b380550b-6621-3061-8bf2-f8d34e79563a | -5.42278 | -60.2166 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fed974d7-4dfd-3161-8a31-4997242a8c8a | -9.27809 | -60.62787 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1b9a07e-2a66-3897-ac8a-1d0a334da6fc | -7.12555 | -48.43773 | 2026-09-21 05:42:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 895c9c2e-aaa1-3353-993f-ceacd523c239 | -9.55952 | -66.01962 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57e9aecc-117a-3cdf-b08b-bfb24d05cc06 | -10.43114 | -50.24352 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6b822710-1a41-31ea-b0d7-330964bf9660 | -11.01553 | -54.1349 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb8635d3-6979-3270-bc6d-e3051db24cc8 | -10.30989 | -50.55466 | 2026-09-21 05:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 618585c9-e847-3290-8810-97b0130f1ba9 | -10.80343 | -50.76946 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cd47795d-0efe-354a-a0ad-f613173bdcc1 | -9.92937 | -58.31202 | 2026-09-21 05:42:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62b18011-469b-3229-830b-f23c4c79cef9 | -9.54935 | -66.01354 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68e2ca7b-aa27-351b-9ee4-350327673a84 | -11.04042 | -54.15157 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| daa12869-700b-3eee-9feb-080b4db3669e | -10.21826 | -59.40554 | 2026-09-21 05:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06983ce2-6612-3070-9b3e-12ae130e1b7b | -11.04532 | -54.15549 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bd4f1e5-3da8-3293-9ffa-dfd0ad6128d5 | -9.67953 | -54.34088 | 2026-09-21 05:42:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ab16553-5c95-3a1b-929d-71e1d89b7e23 | -10.38039 | -48.91175 | 2026-09-21 05:42:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 24e5694b-ca1d-31db-b515-83f2c9cffc8c | -10.42697 | -50.25587 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0b249d3-89dc-3fb9-a0ae-4457d7bb9f1a | -6.19941 | -57.77964 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a03f23c7-be18-331b-9aba-d97336fadd55 | -10.42976 | -50.25551 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| af25520e-a0a6-3571-aae1-b4c0d1a6c800 | -6.73851 | -55.09248 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bea37619-15f3-30c5-8d1d-55b433d2efb3 | -4.32256 | -60.88516 | 2026-09-21 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2034300-caaf-353e-8163-d63a85af2477 | -9.5641 | -66.05954 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96e5c914-1607-390b-94a5-a6338fe067d9 | -7.57135 | -57.67628 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7888d8c5-c688-3e68-b2d7-ebb25cf8de98 | -8.24134 | -62.83984 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1c0c846-1cab-321b-b9ea-ab6d5f361b04 | -5.76559 | -57.58703 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9da7aa0e-c451-3e08-ac6f-f90effc4c941 | -6.45431 | -59.96917 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 04b7eb9b-a242-3183-96cb-4e7b671b3ba4 | -5.82522 | -53.52086 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2937ffe6-86b2-3764-ae9d-138aa635826e | -8.60405 | -54.62379 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f332772-6668-3a02-8ad0-77495be7f07f | -6.16043 | -57.95877 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ff438d1-0e81-38fe-93de-6d0351d52001 | -6.46414 | -59.97457 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a57ac02-e089-3846-9d95-763df5de919d | -10.4244 | -50.24264 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 494d3768-e748-30d5-886a-71bc5845b6d0 | -5.20384 | -56.10064 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b31f7d89-0170-3ce8-bc96-638775da59df | -8.01831 | -71.1418 | 2026-09-21 05:42:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4a59ba9-cc92-36ef-9d5b-6236cee62f81 | -10.92378 | -53.95391 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b00413c2-07e2-3895-9646-650db40e48e4 | -6.77956 | -58.90548 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b01256cf-f8ae-3733-8f0c-b332f74e7020 | -6.13688 | -59.95 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README94.md)
