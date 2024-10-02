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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c8a96da-d73d-3201-92c7-52ec84d1c50d | -22.38926 | -49.29239 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 370d2551-aaab-308f-8894-6c94bc5d221b | -22.38885 | -49.29729 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| cdd5c716-4cbb-3c4e-9d80-3e8344891d2d | -22.38844 | -49.30235 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 1011e918-fa6f-3e3c-985f-a45fb24f401a | -22.38801 | -49.30744 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 378a2a06-db0d-32c7-a280-c38ff303b5d5 | -22.38759 | -49.31256 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f244c301-4813-3152-b076-6fdce5f1e89a | -22.38397 | -49.28197 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 76277e4b-e3d6-3274-afdc-cbe1d2901cac | -22.38359 | -49.28658 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 7e0a7300-a72d-3b68-a8b2-f657728b704c | -22.38319 | -49.29144 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 6813b769-b425-3f31-b837-9c9a6cf1e90e | -22.38278 | -49.29643 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 0d27f3bb-dcd1-3f5a-9bec-188814081cc6 | -22.38236 | -49.30143 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 6a1656f8-392a-32db-bbc1-709f2bfdf76f | -22.38195 | -49.30646 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| fbf1be73-5c0b-326a-9e13-428a7319f24b | -22.38153 | -49.31153 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 60100dea-9326-3ec8-9d56-edcb2d7f1bcc | -20.94957 | -49.11126 | 2024-10-02 05:14:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 96bcdc7e-3bae-3dfc-85fb-12258977a5cf | -20.94915 | -49.11601 | 2024-10-02 05:14:00 | NPP-375D | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bcbe5955-69c4-3019-8345-27322be46593 | -22.37788 | -49.2812 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| e5fd1023-5b70-3e66-b7c8-ffd6e4767942 | -22.37759 | -49.27772 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 48b89f45-8f07-3341-842a-c9669e88f991 | -22.37751 | -49.28569 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| f782670c-b0bb-35b4-b7eb-059bb436922d | -22.37718 | -49.28232 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| ffb431dc-8708-392a-a84c-7ee53429b76f | -22.37711 | -49.2905 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 01c15c21-6c0f-3235-8c0a-25c1f7c9cc46 | -22.37678 | -49.28686 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 74cafa16-1b65-31c4-86ec-9fd0ed68e547 | -22.3767 | -49.29555 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 490f6ad1-6793-33c6-9e50-c95f343e8f39 | -22.37634 | -49.29176 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 6dd21240-8fce-367a-9106-04cf7104c4d2 | -22.37629 | -49.30051 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 2f30a2e3-c098-3514-91fd-78a653908b38 | -22.3759 | -49.29678 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 46442f59-bbd7-3232-9831-a039e1f00190 | -22.37588 | -49.30548 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 9dd445be-5e4e-3a72-908c-5fbca38cf1bb | -22.37546 | -49.30172 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 71fbd4f4-18c9-3801-929f-fa933bdbe7ea | -22.37502 | -49.3067 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 85bf6258-86e3-3dbe-9c0f-328b1872a68f | -22.37219 | -49.27552 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 7bbcd2f9-1eb7-3a4f-8399-afdc7dc1797d | -22.3718 | -49.2803 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| c2b6754c-57d0-3ff2-8f44-898436e56e2d | -22.37152 | -49.27677 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 2fad0078-866a-3283-83ef-b8d2e3f861ba | -22.37142 | -49.28489 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 55b1de4f-0c03-3ec6-8b69-b5a45352539f | -22.3711 | -49.28148 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 3bbb2869-f9a8-3303-b41c-e589a4926e15 | -22.37103 | -49.28966 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| dc9e264c-7ba1-376d-b830-d679e5422198 | -22.3707 | -49.28608 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 2c9c912b-ee23-3211-bbdf-9f5a668d38b8 | -22.37062 | -49.29466 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 955dfa7e-6c7e-3c8f-bc6b-5a8ff2486f9b | -22.37027 | -49.29094 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| ff67072a-af84-37f2-95ad-00f61fa3f570 | -22.37021 | -49.29965 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 35353040-fc2a-3aae-9927-e8c5075bb9c7 | -22.36982 | -49.29596 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 8c485d4f-d846-338e-907b-44a4b85e8ff0 | -22.36981 | -49.30463 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| efb17b9e-3582-3157-b891-b7907c8d307f | -22.36938 | -49.30093 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 7105a322-ead5-362b-8c83-29daa6aed448 | -22.36573 | -49.27929 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| e3bf0c67-9a4c-32ed-a187-f2ebdfdd1478 | -22.36534 | -49.28406 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 085f4288-2426-3bd6-a8b4-351603931c1c | -22.36503 | -49.28053 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2ac65e9c-e432-307a-8296-3204dd3e4d2e | -22.36494 | -49.28899 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 20cafef2-68a9-346a-9137-385be929a48a | -22.36461 | -49.28531 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 82073b67-96ab-35cf-a9a3-06388af8add1 | -22.36451 | -49.29421 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| e1f1f885-f182-34ad-84b9-eb2e37bb30bc | -22.36417 | -49.29036 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4ccbed3d-ba36-32d3-8a0c-2ccef010addf | -22.3641 | -49.29929 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 2fb06243-e70c-3f36-a65f-e1df7babcfad | -22.3637 | -49.2956 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 5abd30da-9713-32de-9479-a7f967e1ef49 | -22.36328 | -49.30929 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 18483527-b4b5-3e90-b97d-8bbe2c06441f | -22.36326 | -49.30061 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| f7ebba72-49e7-34e9-87a5-2475d50c26cb | -22.36282 | -49.30557 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a478d023-125c-37d4-bfe2-37efcdb22a17 | -22.36238 | -49.31058 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| c6acaaff-f74e-39c2-accf-8b3679b7c206 | -22.36062 | -49.33054 | 2024-10-02 05:14:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 433e6d38-cdb2-3f3d-8c96-d0fa875dfa63 | -22.3584 | -49.29377 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| e292f9ec-93b1-3ce1-b73e-e39aacfbedb4 | -22.35805 | -49.28992 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3700052d-a95b-33f7-80df-5123e14e4a24 | -22.35799 | -49.29885 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 57362a01-6b86-3954-944b-872250b9828b | -22.35759 | -49.30378 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| a93d175d-1244-3e43-8a19-7b948783aad8 | -22.35759 | -49.29518 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 46fd157c-82b0-3607-808d-d9076a9574ca | -22.35719 | -49.30866 | 2024-10-02 05:14:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 335c32f5-54a3-351a-9fb3-4acf5baeb0ed | -22.35715 | -49.30017 | 2024-10-02 05:14:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 239b3123-3f79-3c12-b0df-0c511ccc6d2a | -22.35672 | -49.30509 | 2024-10-02 05:14:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 83ab0b4b-b7cd-361b-9318-6dacf72e31e2 | -22.3563 | -49.30991 | 2024-10-02 05:14:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 31bc59da-b69d-33d9-9b7c-8af2562339c7 | -22.3556 | -49.32821 | 2024-10-02 05:14:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| bb8edc6f-d37b-3812-b262-2c10311cf2a9 | -22.35518 | -49.33337 | 2024-10-02 05:14:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 780de838-3c3d-3573-8ac7-282f75ad0d17 | -22.35458 | -49.32946 | 2024-10-02 05:14:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 594d8f53-0d73-361e-8914-6292920211fc | -22.35413 | -49.33459 | 2024-10-02 05:14:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 74896f22-0a13-314b-8a41-b5d34fc82550 | -22.23121 | -49.63319 | 2024-10-02 05:14:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a578817b-d251-3cb7-af74-62bc1c703d7f | -22.22911 | -49.63187 | 2024-10-02 05:14:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fae9067f-4cbd-3b0d-8a3c-6fdce7c92802 | -23.1713 | -49.59827 | 2024-10-02 05:14:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| a9e70eea-f0ad-345c-8d5a-596f81def3b0 | -23.17099 | -49.60218 | 2024-10-02 05:14:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| be2a86b2-c6f9-3a8c-97a5-be218c972213 | -23.16964 | -49.5973 | 2024-10-02 05:14:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 269230f7-d053-3a04-9aaf-4c182ca1a282 | -23.1693 | -49.60133 | 2024-10-02 05:14:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| acb1ca28-437d-3b1f-b2db-374789552868 | -23.16528 | -49.59752 | 2024-10-02 05:14:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 8399b15a-9ec9-35b7-946c-1dc0c7c86ddd | -23.16492 | -49.60205 | 2024-10-02 05:14:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 97f1752f-cc1b-3bbb-9f67-cf81c85b5ccf | -23.16364 | -49.59634 | 2024-10-02 05:14:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 48a162de-5f30-3d25-9eae-7bfc7afb3b21 | -23.16323 | -49.60109 | 2024-10-02 05:14:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 504141d8-72d3-3a99-8c07-989be84ca4ad | -25.03248 | -50.72201 | 2024-10-02 05:14:00 | NPP-375D | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2a2651c6-8243-3cf0-8bb6-f5b557360966 | -25.02674 | -50.72128 | 2024-10-02 05:14:00 | NPP-375D | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9d529f1f-181a-3f0a-abaa-1bc510c2a670 | -19.26648 | -50.84279 | 2024-10-02 05:14:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bd8813ce-7dfa-38b3-834f-03281f61f571 | -19.2661 | -50.84624 | 2024-10-02 05:14:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 050ace40-13ee-3918-86ae-8ed6cf64ecbd | -19.26454 | -50.84198 | 2024-10-02 05:14:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 388b9909-ff7f-3173-8b6c-e7fbbae4b7a1 | -19.26419 | -50.84545 | 2024-10-02 05:14:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d33860d8-8f74-325e-8c79-9d740b7f141d | -18.87698 | -50.86414 | 2024-10-02 05:14:00 | NPP-375D | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 732c92ee-79a5-3b56-9f49-48afc38552e9 | -19.69829 | -51.10423 | 2024-10-02 05:14:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 490188df-709c-3aff-9d10-6819425b3a5e | -23.53478 | -51.13474 | 2024-10-02 05:14:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d572eb31-22d6-3185-b0a2-0c350379ecab | -23.53441 | -51.13868 | 2024-10-02 05:14:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f7efc159-ded5-3de9-a283-1712e4d86067 | -22.63132 | -51.53284 | 2024-10-02 05:14:00 | NPP-375D | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bdcb2c02-444f-32e3-b5ec-d8aa9ae44a35 | -24.73997 | -51.09049 | 2024-10-02 05:14:00 | NPP-375D | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fb2b5bf4-8e98-3ef2-bd73-a0dd9fa009ab | -24.73436 | -51.09006 | 2024-10-02 05:14:00 | NPP-375D | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e9bb331f-d2ad-3fc6-b9e7-c8868de8a392 | -25.61554 | -51.34997 | 2024-10-02 05:14:00 | NPP-375D | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 424ffb9d-85d1-3752-92fa-f0146580772e | -25.60996 | -51.34951 | 2024-10-02 05:14:00 | NPP-375D | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d6371067-85d5-36f7-9b72-f75aa9b76033 | -21.34246 | -55.69497 | 2024-10-02 05:14:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19084ad8-6b04-3e9b-9a40-45cce0c31952 | -21.34177 | -55.70032 | 2024-10-02 05:14:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d726a39-7bb4-3a81-96ee-0eefe41992c7 | -21.33847 | -55.69429 | 2024-10-02 05:14:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 757a2d3b-cd83-3cd6-93e2-5c6b786ff268 | -18.89448 | -54.50663 | 2024-10-02 05:14:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f9e5791-7a7c-3d22-97c0-19a896906c24 | -18.89082 | -54.50198 | 2024-10-02 05:14:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 647df727-dc98-3c23-a44b-e3d10181cd72 | -18.89031 | -54.50599 | 2024-10-02 05:14:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2353aaf-cd43-3c4c-adac-d7cd6e5e98ec | -18.86794 | -54.51505 | 2024-10-02 05:14:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2335eb5f-082a-3ff2-a56c-56cd3322c055 | -18.86747 | -54.51888 | 2024-10-02 05:14:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README163.md)
