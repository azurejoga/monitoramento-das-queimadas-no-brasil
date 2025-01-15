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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfaa5d2f-43c2-340d-b8ae-038de27f4fba | 1.32593 | -60.03974 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ece2f868-42c1-3944-989c-f5723990324e | 1.32078 | -60.03147 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d5541007-7c8a-39d4-befb-08caa3306301 | 3.07758 | -60.75605 | 2025-01-15 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 192b11ff-10dd-33e0-a578-5b9eedfb1106 | 2.28635 | -60.21361 | 2025-01-15 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 18ee1641-03b8-3105-8c64-1c9aa5b9e5f3 | 0.64654 | -60.50376 | 2025-01-15 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8aa4ba38-e9fa-3ad6-8a31-9b8391ff7f1f | 2.19774 | -61.80772 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc22b868-2420-360b-b1a0-ecef8eb96369 | 2.52751 | -60.99072 | 2025-01-15 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2db7403c-7e5f-3efb-b63b-30c6e964389f | 2.1099 | -61.82469 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9b1cbff4-4720-3ce4-a542-7c360d566c03 | 2.08888 | -61.84671 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee8c00dc-1dcc-3bd7-bf47-74549ca25287 | 1.17407 | -60.49002 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 163ca05c-f4b9-31c7-9c70-8b62c503d66e | 1.17474 | -60.49424 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25573cd9-eaa1-3bf5-bb47-da9370ec49d2 | 2.51637 | -60.99156 | 2025-01-15 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 63f3dc4c-56f7-3565-b2b1-f7f31719cae3 | 1.9369 | -60.41063 | 2025-01-15 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a897628-e251-36c1-a1e6-c2647d741ff8 | 3.04265 | -60.23673 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 919e011b-1b91-3d45-9e42-f7f508db49a1 | 1.35065 | -60.02677 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5a0fd59-cbc2-319f-90b6-80be93e237a6 | 2.18125 | -61.81409 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67b3e803-7958-388b-9110-e52494f33b2d | 2.09051 | -61.81267 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 736b7382-ab91-30ff-9d36-b44405ebe701 | 0.72799 | -60.11668 | 2025-01-15 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f722926-9c53-3f47-b45d-a40ac9805e3b | 1.31492 | -60.43862 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ba88446e-2489-397d-8772-2fe6736acbd7 | 1.1734 | -60.48581 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07197ef0-3018-3423-be28-c3a68acbec8b | 3.23559 | -60.18306 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e6fd5c2-2501-33f3-899c-bb7ce3f1fff0 | 1.32588 | -60.4369 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da3c4d09-8d8a-31ad-9b83-7e97686c258b | 2.10078 | -61.81114 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a92a1d6d-98ac-3ac7-a48b-8e1b0c47c072 | 2.28236 | -60.21606 | 2025-01-15 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.4 |
| ef3275f8-cf95-33ee-b395-0c8c6eb4ce5f | 2.28702 | -60.21786 | 2025-01-15 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 345afd0a-7ab1-3ee4-a036-2b7d9b9ae7d4 | 0.66551 | -59.59155 | 2025-01-15 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4577ecc3-41c3-3c89-b560-0275244eac1d | 3.08958 | -60.71784 | 2025-01-15 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d02a6092-6818-3913-9e87-232dbd38b0bb | 1.17042 | -60.4906 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 30514de6-f36e-3bb5-ad04-3af99eec1d2e | 2.09172 | -61.84253 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a2c6b0c-eacc-3dac-81ee-9320a807bc3a | 1.32149 | -60.03587 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ecb0e95-911b-3320-98c4-2284bd251971 | 3.23493 | -60.17891 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c49bde6f-040c-36ca-9124-6c119884f4f5 | 4.0488 | -61.14863 | 2025-01-15 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f820c1a7-3f65-3871-9cfd-7d73f26f72ac | 2.524 | -60.99128 | 2025-01-15 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9edb5195-7603-34fd-9976-716a4dd06771 | 2.52049 | -60.99183 | 2025-01-15 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 3f5773ee-1ee2-3b19-877d-795e23ae0e27 | 1.32023 | -60.42479 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c7a3eeda-b662-3ce2-9911-92c35da065e8 | 2.52338 | -60.98739 | 2025-01-15 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| adfcb7c2-e609-3d05-9d96-495b918c28f0 | 1.17906 | -60.49786 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f60f7b4c-37d7-3019-8d24-a94a988e8faa | 2.0985 | -61.81895 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 227920bd-991e-3efe-9283-6beeadbf9f9d | 2.94075 | -60.18044 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 036b3d5f-e3a6-36eb-9925-3f64308e6475 | 2.28601 | -60.21548 | 2025-01-15 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 2580c8b1-ee19-3c1c-a9f7-ce9e30ddf5de | 2.2827 | -60.2142 | 2025-01-15 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e16cc6ad-94a1-3ce6-b242-950bcb4895ae | 1.01469 | -59.56795 | 2025-01-15 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a486ee96-7238-335b-912c-09c64bd4a07c | 2.51761 | -60.99626 | 2025-01-15 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 955c7766-dbaa-34ec-b01e-8a1a63fa49f8 | 2.09855 | -61.84149 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 31150d4a-c0aa-3011-bb41-ea4eeead6ad6 | 0.96691 | -59.47455 | 2025-01-15 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d34c4f54-afac-39d8-8335-6a412e7870b5 | 2.34483 | -60.23219 | 2025-01-15 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f83997fe-c7b0-3fdf-9513-c4b3f15a97b2 | 1.17839 | -60.49365 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1923f6f-6e62-3791-929e-1772dc7c4cbd | 2.09109 | -61.81635 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cf83621-3028-3009-b64d-9150a89ce64e | 2.51225 | -60.98823 | 2025-01-15 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb6d461b-cc1f-365b-a60c-8d6bcedf3623 | 2.11015 | -61.82901 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 79931aa0-ce0d-3c64-a23c-3272ade6d746 | -1.47438 | -54.19571 | 2025-01-15 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99b1869a-fd83-3d67-8857-5ea9a57b5e8e | 1.32289 | -60.44171 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b7a39224-f126-32b3-bf6e-e9bad9c44365 | 1.31193 | -60.44342 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e35c2937-f2a6-3493-9486-69ad4f763f4d | 2.10533 | -61.81788 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1593385b-8265-3906-91c4-756d55fc9964 | 2.11048 | -61.82835 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2796bb12-9816-3357-a3c3-dfc90cd6cb06 | 1.35136 | -60.03121 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae712c92-a77b-3540-a207-8eb134c3434b | 2.0883 | -61.84305 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d118cb6-09b3-3c15-a1b7-b22a94ddafdf | 2.09513 | -61.842 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b2a3f11-4964-3c20-a639-a9fa3e368753 | 2.18067 | -61.81042 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acfdde5a-8a24-37b9-9ade-9af5422b92d5 | 2.09056 | -61.83519 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd8481e5-ca7c-34ec-8b9d-21e80abd851e | -1.47478 | -54.19381 | 2025-01-15 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07837933-f72d-3725-9534-9f9313beac91 | 1.31956 | -60.42056 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6e4e8990-d869-3c01-8d81-47eb7bb062b8 | 0.72354 | -60.11277 | 2025-01-15 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0237de1e-def8-337c-8c22-c1378dbf6a82 | 2.51987 | -60.98795 | 2025-01-15 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4393465a-5872-331f-8367-b7ef8171a9cc | 1.18137 | -60.48887 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cd2e9aa-eeb1-3cc3-9e4f-2f14d3c1f3a7 | 1.31127 | -60.43919 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c078a7ed-7018-3cf9-8a3b-faed34460882 | 2.19491 | -61.81194 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 642cab42-f101-3e21-92ec-0666e697ad30 | 1.11716 | -59.4611 | 2025-01-15 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a28911c4-6f92-386f-917d-057befa58362 | 1.32223 | -60.43748 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 238c5dc8-2e2c-3e57-ac65-9de2314a1d59 | 3.23197 | -60.18364 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 468cc8fb-3e6b-3613-8936-35e151ec24ab | 2.09797 | -61.83782 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a47454d9-7c58-3af5-908c-465699d9827c | 2.94801 | -60.17927 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e849d59-99a5-3901-a299-6d0e53752da9 | 2.51286 | -60.99212 | 2025-01-15 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04653127-3a4f-360f-b626-7bb519b5dde3 | 1.17772 | -60.48944 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53611618-2b21-3986-aed8-211d24065e46 | 2.10875 | -61.81735 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1486ea4f-1042-376e-b62e-49bcced308f1 | 2.94438 | -60.17986 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11da2dda-e250-3755-bd84-1c51f080245a | 1.17705 | -60.48523 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6194009b-93a2-3a4e-9639-c58439b47b0c | 1.04635 | -59.54349 | 2025-01-15 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2c0e32b-7de0-3e0b-a8d9-262f10e47946 | 2.09167 | -61.82001 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d7970ad-6027-37f1-80a0-da473738cb0b | 2.10591 | -61.82154 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2680f4cc-da7c-32f0-9715-418694ffba70 | 2.94506 | -60.18401 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb4e20b4-daac-3511-95a4-13c5e7eb3496 | -1.46926 | -54.19087 | 2025-01-15 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bb74f3a-b403-3f6d-b110-70568551f1b0 | 2.2867 | -60.21973 | 2025-01-15 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 2c395c68-726f-3453-a20c-3812015291ab | 3.04034 | -60.24559 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f4360b1-39f0-34d4-b493-4fcbc990f7e1 | 2.09735 | -61.81165 | 2025-01-15 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a8abe355-6a8d-3f3a-9edf-3b677cd8c3b5 | 2.28531 | -60.21122 | 2025-01-15 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a00f6dd-a1b4-37e8-b2dc-f3ec34f4a348 | 1.32356 | -60.44593 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8e77b515-a726-3c2f-930b-b67160850e75 | 1.31924 | -60.44228 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6fed910c-6e33-3e69-886f-3486e6555c8a | 0.72729 | -60.11219 | 2025-01-15 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28111bfc-23a9-3a1a-b1c3-95861514e430 | 2.94936 | -60.18756 | 2025-01-15 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8cf174d-7167-3125-8b24-8fc64d2a8608 | 1.17542 | -60.49844 | 2025-01-15 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3963b0e2-30b3-3a19-9ec6-b0b7e5bc3432 | 2.5205 | -60.99491 | 2025-01-15 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 58dfdc40-7750-397b-923e-496f9fd1acac | 4.04939 | -61.15236 | 2025-01-15 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8aa81ab-f557-30a6-9416-97bc011bb0fc | 2.1039 | -61.8166 | 2025-01-15 05:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0a92f364-6827-39e2-9c28-acb2ed716cb1 | 2.5247 | -60.982 | 2025-01-15 05:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 67.1 |
| eb27a5df-b33d-3481-91b2-5220e596661e | 2.2889 | -60.2076 | 2025-01-15 05:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 45.2 |
| bc403e35-8bee-381f-b617-56dba15b8cf8 | 2.1038 | -61.8354 | 2025-01-15 05:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 61da56a1-f7ce-3c40-9b78-84acc235bb44 | 2.5247 | -61.0009 | 2025-01-15 05:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 0bfa4635-fb79-3444-9828-627b0bd58e5f | 2.1038 | -61.8354 | 2025-01-15 06:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| fcb75a5a-70a8-3b0a-a616-ded949cccf80 | 2.1039 | -61.8166 | 2025-01-15 06:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 70.8 |


[Clique aqui para ver as próximas entradas](README7.md)
