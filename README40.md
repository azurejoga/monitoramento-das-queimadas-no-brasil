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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d727360c-1a0a-33fe-8fd5-f35377f11a92 | -3.20965 | -58.85445 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1585619c-74a4-3006-b60c-a0f08cb197b6 | -3.50727 | -60.21869 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 0ffafdce-7190-30e7-8a8a-af85bed06b15 | -3.19149 | -58.65768 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| a0b3a933-bd63-3c77-a7f3-7f4267c8333d | -5.22513 | -60.04837 | 2026-10-09 00:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bc10a327-4c66-3af3-a359-7015ed27a550 | 1.21567 | -59.98355 | 2026-10-09 00:37:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 10be1c73-57a4-332f-b9e2-9ecc35e3c6d3 | -1.14963 | -54.23121 | 2026-10-09 00:37:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 831b46e3-d3bf-3195-a428-bee331fe461f | -3.55388 | -54.68544 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 26227b23-1f6d-3a16-8ae2-a26a5c87284d | -2.50176 | -56.06565 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 7c2a9e01-0279-336a-947d-86008a5a53e4 | -2.73667 | -54.11387 | 2026-10-09 00:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 2e7b9681-2753-3c5e-8467-2722f13c58db | -4.39279 | -56.04961 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 098b5d13-e4c5-30c6-a13d-d4148ce3e309 | -1.11836 | -54.18262 | 2026-10-09 00:37:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| e4b735dc-7533-32a1-a949-fafd16c4d859 | -3.86239 | -55.98867 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f4896890-70f7-3d75-af28-e8d03c07f2c6 | -3.22373 | -54.30728 | 2026-10-09 00:37:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 1a142a97-cd3a-3b7d-8bdf-9ba48c82afb6 | -3.18137 | -58.64999 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9c33c561-3361-36ea-83a3-0664a3318086 | -2.23135 | -58.11054 | 2026-10-09 00:37:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 541d880f-7c30-302f-8ae2-61547b9f1958 | -3.45531 | -59.56095 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 202d0c78-f8e5-3b3d-8286-26d4dc7915ce | -3.65672 | -59.16268 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f89b262a-5cdf-38c7-919d-fcb568464d41 | -3.63473 | -60.61048 | 2026-10-09 00:37:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 77a333c1-d93b-3768-833f-71095ebd2473 | -3.78019 | -58.57778 | 2026-10-09 00:37:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 64da5b73-ae5e-35cd-9166-68f7e8836f81 | -2.47682 | -56.09945 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0cf2862c-88c6-31d7-a514-81affeb566f9 | -3.30636 | -54.02207 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 6a590245-7c38-37c5-9fff-2ab065a15da4 | -3.45651 | -59.56974 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| e362ed83-7dc9-3e07-83cd-87d28daa1d6f | -3.74687 | -59.47532 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 9bd24863-a628-3541-8e10-a2f0d1b25f27 | -3.70464 | -61.33461 | 2026-10-09 00:37:00 | TERRA_M-M | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c6a4e77e-137b-328f-9108-8ba137b022e2 | -3.02275 | -54.18742 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 03fc4d90-965c-30e7-b1c5-5b6f19297cc6 | -1.20108 | -55.68328 | 2026-10-09 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5f07a928-438c-319e-94c4-349572ef5c00 | -1.46245 | -54.76332 | 2026-10-09 00:37:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 3835902b-a988-3b4a-9471-dec237367f35 | -2.93105 | -57.6477 | 2026-10-09 00:37:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9f58eaad-58a6-350c-874a-0bc566bb750c | -4.06479 | -59.84402 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4539fc52-a547-35cc-89c4-e9d74f2b4de3 | -3.30251 | -61.01255 | 2026-10-09 00:37:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4606f04d-1bb0-3284-8e4c-5e81d4ce1e4a | -3.72237 | -59.36239 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1229f966-cb67-3bec-8ee8-b8ae6482b8be | -3.46838 | -59.26391 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| a3a32754-3eae-3245-a968-cfb209f1c3c2 | -4.11639 | -59.89116 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ce7ddf9c-636e-3b44-b038-19ce308aebb7 | -3.89481 | -58.94978 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 55749a71-64c1-336a-acbc-fda40ff066e3 | -2.90909 | -57.21921 | 2026-10-09 00:37:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a96a1c4b-fb93-3d3d-b346-597d8344c62d | 1.6911 | -55.62119 | 2026-10-09 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 84d28edc-4076-3dc7-931c-d1eabb11cbdf | -3.18187 | -58.84932 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 19ec4aec-6ac4-3059-895c-cbbcd513155e | -1.11597 | -54.16538 | 2026-10-09 00:37:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| e2c18f43-4cac-3a47-b25a-39ce5e671d07 | -3.78264 | -59.19555 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e083f11d-cf60-37f3-b0cc-882dca74fdd7 | -2.8423 | -54.12641 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| b9a66f87-8d1d-3f96-bc05-dc70c4a4eb45 | -3.32275 | -61.30194 | 2026-10-09 00:37:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8bc0823b-5baa-3760-8234-982641a2a466 | -4.29781 | -60.95405 | 2026-10-09 00:37:00 | TERRA_M-M | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b1569b88-f697-3718-b1bd-065698184293 | -3.36125 | -59.48194 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 91fb0030-0fae-3297-8697-4a149a558f82 | -1.77597 | -55.03429 | 2026-10-09 00:37:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2fe54e63-1fff-3a67-a4d1-837dfb3eb876 | -3.7121 | -57.10096 | 2026-10-09 00:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d6b02f77-639e-3cb6-80ef-a1e7f748fa73 | -3.42538 | -60.2268 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a1697bf3-954b-3c19-956f-9c6b49700170 | -3.52594 | -59.33939 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 6766ecd3-2561-351d-a9a1-73465911fe97 | -3.52826 | -59.56868 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e43316fe-310a-3a90-a11c-e82470e29562 | -3.63318 | -59.3181 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f393bfb5-51a3-359b-a391-b8218148ac87 | -3.77059 | -58.8473 | 2026-10-09 00:37:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 06aee4fe-4de4-36fa-862e-059edabd19a6 | -3.90079 | -59.45053 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| bbf0d8a0-d963-3576-a5a8-4b6e6829d61b | -3.17065 | -54.7364 | 2026-10-09 00:37:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e5d2d45d-f38d-383f-9a05-2134eba8e916 | -2.87499 | -54.18814 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8b8eb9b2-c11f-360e-a7e1-4754ecb2d125 | -1.62782 | -55.12691 | 2026-10-09 00:37:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a700c11d-74fe-3b85-8386-66b591cebf06 | -2.62822 | -57.71492 | 2026-10-09 00:37:00 | TERRA_M-M | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e75be867-31ca-3a6b-a100-8af822b9060e | -4.32675 | -55.01896 | 2026-10-09 00:37:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c6d6eab3-8712-3d45-a695-47a3d3bd6564 | -3.59699 | -54.58425 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b4da831e-b8a7-3de2-a415-e20ad46da04e | -3.09322 | -53.95271 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| be5f96a7-ba03-318c-8dbb-d33e7e661b22 | -3.73926 | -59.48534 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 04461a5d-b95a-3fcc-ad8f-1dd2c3156117 | -3.16112 | -58.63464 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| eb3724c3-768f-3c83-bcd9-eea2ac0fcdf8 | -3.56707 | -54.69831 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| bed595bc-ec00-3f2e-bed3-538c85428cde | -3.79074 | -59.31971 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 679cc025-3c3a-32b9-b332-9df14ee02a75 | -5.24498 | -60.19423 | 2026-10-09 00:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e643985b-d3ad-3055-8a21-0c12f96826f4 | -4.28863 | -60.95531 | 2026-10-09 00:37:00 | TERRA_M-M | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 43850e1a-55b8-342f-bf1b-0a2cd0aae6d2 | -3.5921 | -59.42855 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4a8c317d-2a43-31d5-a5cf-100fceeb2144 | -4.80362 | -56.13724 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| bca862a0-246c-37ce-b433-9a50d53a5616 | -3.47194 | -57.49507 | 2026-10-09 00:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a37a6540-784a-3fbb-8759-504783be9888 | 0.78843 | -59.1989 | 2026-10-09 00:37:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 49c74473-33fd-3742-8af4-761704b186b1 | -3.43305 | -60.2166 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7c3f7acf-0949-35c7-9090-ff7bedd0079a | -3.09305 | -58.01362 | 2026-10-09 00:37:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 44ad9d91-7335-31ac-8c0b-00ef0d3a010f | -3.46764 | -60.26074 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4418df9f-154f-3eea-85fe-69089cdcca12 | -3.78268 | -58.59561 | 2026-10-09 00:37:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7f61e19e-ac16-349a-9476-2272c98185f8 | -3.10263 | -54.18567 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e961154d-4270-3bcb-b64e-31931570633c | -3.59836 | -54.67885 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 7ef7b385-d7be-3f02-936a-01afe8ace49d | -3.58724 | -54.68048 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b7ba7e54-05ff-38fe-93f8-3e32ec959156 | -3.73685 | -59.46777 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 2be900e0-f754-3724-9301-275e0c78596a | -3.74724 | -59.41261 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 64f657a7-2d37-3bfa-ae9c-248c44d37d57 | -3.62667 | -54.22475 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| cfc6d4c3-3942-353f-aba4-79bfe7c93d3f | -3.58166 | -59.07465 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 49cf4467-39e2-3117-8ba9-80e8dfbcb5d8 | -3.54488 | -54.70173 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 939465c7-b7d7-356e-b518-edae87ce010a | -3.89833 | -55.88196 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5f9b8759-af92-3f96-bdbb-768dc3781519 | -3.70128 | -60.55797 | 2026-10-09 00:37:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1161b940-91bf-31d1-994e-55511e0be1e9 | -3.00876 | -54.0899 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 1deeec02-9639-3a5a-98cb-6a25c71f5d3c | -4.12648 | -59.89882 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 047107e4-d746-382f-8241-28cfaad8fa4f | -3.55285 | -59.46982 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2b8dd48c-b768-3a27-9ce8-3f16732ea438 | -5.21619 | -60.0496 | 2026-10-09 00:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c06efa56-06a8-322f-a89d-e5018b1b6190 | -3.09085 | -53.93607 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 5655335c-45bc-31c8-8a14-e3c7ca3f8e9d | -6.04643 | -59.9262 | 2026-10-09 00:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 49e271c3-c65d-3360-b825-645d6de9d915 | -2.87727 | -54.20435 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ac5ce73e-6944-3a10-9419-5f8089f2561c | -2.72986 | -57.46006 | 2026-10-09 00:37:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a5ecda37-2239-37ac-9ad6-13f19de7c934 | -2.49347 | -58.07465 | 2026-10-09 00:37:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 2575ea50-b6e5-3bdd-a93b-6c758fff6ab9 | -4.07243 | -59.83391 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| fd1f9e7a-9103-310b-b33a-06327e745a35 | -3.35123 | -59.47439 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 505885f1-7d85-3560-9910-40ffebe4c1eb | -3.83063 | -55.98133 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 8d7a1c29-8611-3ea8-8847-16c605c9d754 | -3.34255 | -50.40548 | 2026-10-09 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 7be0f1e9-ddf9-3081-8602-292906c6a761 | -3.3931 | -61.07134 | 2026-10-09 00:37:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| dd575147-c091-37ca-92ef-0950677e6a68 | -3.71192 | -60.16893 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 41d2a3f6-cb01-37b9-96a1-c680d3f7265d | -3.63849 | -60.63808 | 2026-10-09 00:37:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 45937028-ce40-33c5-bef9-3de91d87048b | -3.10276 | -53.93437 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 6216a4f1-7120-3218-9131-5fa2858a1a22 | -3.18064 | -58.84046 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |


[Clique aqui para ver as próximas entradas](README41.md)
