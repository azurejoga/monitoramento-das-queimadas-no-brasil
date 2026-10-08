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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fefd1e9-fde0-3238-a803-f0b560c6dabf | -2.50297 | -56.12847 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a1060c7-9f89-3602-b4b2-a5fa0e897bc9 | -3.10712 | -53.78014 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 051fe829-6556-31df-8e50-cb455f2a69ee | -3.58268 | -54.68127 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c510489c-a2f6-3873-9661-826618c9d41d | -3.84099 | -55.98981 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5c0ab17-e5e4-3c36-bd5f-cb81458f3a9c | -3.46999 | -59.58179 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef804ad2-27b7-364c-80fd-63f47d4c1b1f | -3.2019 | -50.54798 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 50ee0d3c-6ae8-303c-a4d0-447e998ea23e | -8.51764 | -67.0005 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f308591-475a-399f-96c1-f0f34f41e340 | -3.42966 | -58.59725 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70ca53fe-19c0-31e2-b29b-3582f8006798 | -10.99015 | -54.22169 | 2026-10-08 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32cfc3ed-9b0d-37e7-b2fb-c42c04b916e8 | -3.73346 | -55.98388 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 229e68f4-7055-33e1-9bd7-12ffda454ca0 | -2.55052 | -56.29507 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e464eb8-0b98-3935-8de6-0adae4f7e5f3 | -2.98084 | -54.12246 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6f3c7160-0ae3-38f7-8fd9-76db403d4ab9 | -2.57464 | -56.16433 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c4ae5da-d363-3553-b591-71633706d74a | -2.53691 | -56.42386 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc7b34f6-47e9-30c8-a256-7c1e22ae240d | -2.2216 | -53.70351 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 57e9a86b-4957-302d-8a9b-e66e1276f4d9 | -3.65514 | -54.28503 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87ab149b-91ef-390f-95ee-4c400249bb02 | -3.27095 | -54.02205 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b66fc8a0-ccc4-3221-8ec4-26e36944f740 | -9.16749 | -61.40639 | 2026-10-08 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f988b541-7f8b-3c3b-8c6d-6184aba947cb | -3.27494 | -54.04271 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77391b37-024e-393c-83e8-3074e132f1b4 | -9.07315 | -65.48267 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1792af5-9fcc-330b-a316-3e163f25a8f6 | -2.31895 | -57.98577 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 008a24d7-881e-325d-8a35-e6dedee6eb94 | -7.0817 | -52.67863 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 124fe04c-5270-3128-b0b2-9dd01486c1fb | -3.40893 | -59.58587 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12ccbb3e-1784-3a2b-a880-b85fc2c35cb1 | -3.06017 | -54.17022 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 285b005d-e96c-3a65-b3d9-fb7713a65057 | -4.93227 | -55.86771 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe907023-fa58-30e0-9812-4ad0fc237629 | -3.03217 | -53.93495 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5eb523d-cda5-33f2-bf38-5822861a2cc3 | -4.41898 | -55.75553 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2183a63f-023a-3234-a041-939597bfc3db | -6.16296 | -52.6551 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 066b589d-08f6-30fe-8361-0c8eadd71dea | -4.57676 | -54.95324 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 072ac950-b9e6-381a-ada1-d879e47e32c7 | -3.66782 | -55.54098 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f7503d5-d3d9-32cc-a7f3-b992e16dc021 | -2.48974 | -56.1689 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55245d6c-bf10-3e5e-b24f-e475b50ab6a6 | -2.98763 | -54.76233 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3930fddf-0abf-3e21-9b0f-f1c433fc0555 | -3.51583 | -54.66383 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9b69bbc-309c-33fd-81d8-fc429d41dbb3 | -3.27601 | -54.05889 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fc70167-f419-3ca1-b1b3-1a2fc27f418e | -9.13765 | -65.29056 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a41c41d0-266f-3d41-9949-c4982b4176d9 | -2.99717 | -54.18392 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5e7a7f0-4898-329e-82b8-144867b20aa1 | -1.18802 | -54.17636 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6860b127-607a-3145-85e9-86ec50067b94 | -6.24121 | -52.88026 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad6bd1fa-dca2-36c4-bc5c-b88d0511e108 | -3.44714 | -56.93605 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 561373ad-2b0f-379a-abe6-8bca60b5e5b0 | -2.99111 | -54.75834 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46562fe0-383a-3f82-97bb-fc8a9a29c140 | -1.41617 | -53.23046 | 2026-10-08 05:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d389fd8-cfa5-35a7-91d7-a0a0a5550cc9 | -2.90136 | -56.66922 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0c2b533-0228-3269-a348-9ca09aa03652 | -8.60152 | -67.30919 | 2026-10-08 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f4df137-902c-35c3-97b2-8257e5b9bafb | -3.03207 | -54.07487 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f62d135-b7e8-3312-a5eb-a0a89e238afb | -3.03461 | -53.9192 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 310f0362-63e9-30ae-a47d-5265b3c0f7e2 | -7.14711 | -46.52192 | 2026-10-08 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7ded6b6-4dca-3ab6-95db-56c6ea878a47 | -3.421 | -59.56555 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 662ff719-1271-385f-ac71-bc08069c13a9 | -4.2798 | -55.13081 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb199a32-96f8-3172-bc77-b1775b9bbc7f | -3.21886 | -53.96162 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17582a4a-9d08-349e-b0ed-9d960b77b484 | -6.93162 | -43.66681 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7a211385-9fe6-3155-be2a-a87da6683ffc | -6.9245 | -43.66558 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8efe4ef3-0d88-3b72-bb1e-5918c50702a1 | -4.85991 | -42.83429 | 2026-10-08 05:23:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a97a250b-be4c-3c16-8a40-f2306ae25696 | -6.39214 | -52.72357 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6542538d-9760-334a-8445-1f8fb19a95ef | -2.99911 | -54.12523 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ed64981-d724-3b42-a442-2dbe8688a3aa | -2.86779 | -54.47797 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 758de2eb-08c3-3547-96c0-176dcccde6c3 | -2.41122 | -51.30213 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef72bd9d-81b1-3670-a854-dbb3ff2210a4 | -8.5982 | -67.04372 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a736a73-0d5f-36f3-a71c-168e351bc9e4 | -3.26342 | -50.40472 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d456fbf4-e849-32fc-8b38-2a1a122d7961 | -3.85598 | -55.95997 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6f987dd-7cd5-3785-bab9-3e5b3f92ee46 | -5.29701 | -60.09588 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 497ada59-d205-34d6-a7f6-e5de874bdc9e | -4.00819 | -56.25836 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab938f24-acb8-3386-961b-88a5f2119ea4 | -3.03376 | -54.08704 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 02ce153c-335e-3dfc-898f-0f83eacd4aa8 | -2.57245 | -56.17815 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b666b99-9c2c-35a5-9e1b-aad69d89fc46 | -3.48378 | -54.62047 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b5afdf60-6644-3400-bff9-1b9dfa2fa9f2 | -2.98757 | -54.08002 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b59ee0ae-98cf-3918-992c-3dd7da3bce0f | -4.44992 | -47.92366 | 2026-10-08 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 855dde84-0587-3fa4-9ea8-e4c95cbd8aa0 | -3.50044 | -54.62692 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9502a29b-c044-3108-b8eb-375f4d1bdd44 | -10.66687 | -58.92492 | 2026-10-08 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cb10a31-50f2-38db-ae70-41bf125ac8cb | -2.49909 | -56.13141 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fade5ae5-e782-36f9-9546-9112cafdc09b | -2.98484 | -54.7762 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d60fadb1-2a9f-3777-9e7d-496b58e821ae | -2.73845 | -57.60978 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8db23a1-3981-366f-a35a-ad654fdfc36b | -3.04705 | -53.90902 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c538563-91aa-39ef-844a-1adbc5d2b13a | -7.26008 | -48.06633 | 2026-10-08 05:23:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57ff3eeb-7e8c-3044-9812-9347505a8bd4 | -2.46848 | -56.06636 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b37b662d-547c-3c5e-ac2d-960d22704c95 | -2.86388 | -54.20659 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 886aca15-6d4c-33cf-add5-e417763071e7 | -3.5485 | -56.84965 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c323d2ec-7678-3317-992a-7cbd0619d157 | -3.00117 | -54.04224 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db784b9a-b25d-3ba3-8689-68267ba30303 | -5.30199 | -60.0882 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61da472b-033b-3496-a8e4-822941df1783 | -3.51168 | -54.53251 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3545a36-709a-349c-a9a7-35e651f9c67a | -3.00057 | -54.04613 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f186b2ed-9b36-3330-9aad-6fc0eb19183b | -3.53493 | -54.63229 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1033585f-09b6-337b-8037-b4cabd51cf76 | -5.74051 | -45.15762 | 2026-10-08 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f1f3c726-a070-3a9c-9b85-b5c43c346b74 | -2.90036 | -59.22372 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07fd584d-8999-3d26-bf0a-fae2de862597 | -2.46187 | -56.0866 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b87eb83-5f1e-3388-908a-a823cbf47730 | -3.22313 | -53.89048 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 473789c6-53ad-37bc-b798-7c1ed0ef1444 | -6.46837 | -55.47964 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f03fb28-4e92-3b47-9ff0-08001188677e | -1.52102 | -54.5648 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1d11c27-4d63-361f-848a-24bdb476aeb9 | -3.71009 | -55.9802 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1acf1905-9815-316a-ba47-fab72c4cdc4d | -3.93384 | -54.57623 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f38dd313-aaaf-333c-a6a2-00dad57c4b0f | -3.16323 | -54.73197 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 875b546e-fee6-37ee-b758-de5de8db3b3d | -2.50301 | -56.14973 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dacf657b-65fb-3ad1-8271-2b28e83d9a8d | -3.54726 | -50.09929 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01e5bef0-8fe5-3e71-a0e5-299a7b36c178 | -3.02664 | -54.1097 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1b159a97-d6a6-3990-84c5-c84c14f8157e | -6.10416 | -55.69158 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ef44b54-43f0-3e9c-836b-e6e7dfb555cc | -2.99525 | -54.05724 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30a026bb-0d6b-3d7b-a3a5-d9ffc68e3162 | -3.10082 | -53.75056 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 229607da-2a26-3b2d-91e9-2704836e7501 | -3.31763 | -58.26892 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a70d563b-0743-3f11-a832-146157df92e7 | -1.19734 | -54.13966 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e74c7ff5-5023-3183-9b83-b261df197408 | -5.87502 | -50.09912 | 2026-10-08 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e2a14faf-42e8-3842-9762-7338ad55abba | -3.30146 | -54.03475 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README134.md)
