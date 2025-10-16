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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93b2cfe6-71d6-3a16-ba90-ab6174f52c02 | -6.75563 | -44.39044 | 2025-10-16 12:00:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| ffa98371-5305-326a-8a80-e46da3791b39 | -7.85597 | -45.415 | 2025-10-16 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6ddabb93-d1cb-3843-8d43-f7294674d190 | -7.33553 | -41.19929 | 2025-10-16 12:00:00 | TERRA_M-T | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 9e20f95b-5f28-3e74-a80d-235428000c62 | -6.7981 | -45.48257 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4578a080-a9bc-3dde-854c-6c53f5c6d2df | -11.46552 | -44.18113 | 2025-10-16 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 79caa93f-f34d-398d-821b-158c290c141f | -7.17717 | -42.18438 | 2025-10-16 12:00:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| fc399100-985a-30bb-b844-d1ab3dc8658b | -12.27704 | -47.14378 | 2025-10-16 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| ab225815-a4c7-3093-99fc-f55fe1f775d6 | -6.94718 | -44.47082 | 2025-10-16 12:00:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 36e0a302-b073-324d-ac78-8929cdd719a0 | -12.26057 | -47.11668 | 2025-10-16 12:00:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f96ae863-e6c5-3d8f-9d21-044d7eaa0365 | -7.53801 | -44.27996 | 2025-10-16 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 67be543e-586e-3a5b-9aed-fb6081f75410 | -14.12185 | -43.46594 | 2025-10-16 12:00:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 70b40512-7b6d-3a9e-84fa-c2159e0dd55c | -11.49513 | -44.10242 | 2025-10-16 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| bc2237b5-5be5-3c78-8b6d-e6cd28394f00 | -8.56364 | -44.58193 | 2025-10-16 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1533c11b-65c4-30d7-9755-4283010d66cc | -9.2498 | -45.2928 | 2025-10-16 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| f170fc90-141c-3993-8e46-3b16f73cb331 | -10.69999 | -44.42777 | 2025-10-16 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 475c0fe8-d548-34d4-bc41-4eaeabfefeab | -6.80953 | -45.47294 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 2b2da514-9eb3-37a7-b7da-75ab83c9a631 | -6.61895 | -44.43486 | 2025-10-16 12:00:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fc62c1c1-ff7b-3347-9575-87fe52c45a8c | -7.12339 | -44.27278 | 2025-10-16 12:00:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5c40523e-e922-3388-9262-b6c863343340 | -12.96157 | -47.09527 | 2025-10-16 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| d7a3b7b2-213c-31d1-af94-7d19ced17386 | -9.69059 | -44.51364 | 2025-10-16 12:00:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 89cc0881-707d-309d-966d-ecb583ca113d | -12.99084 | -43.45014 | 2025-10-16 12:00:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| c3be2abf-0fb0-32db-9876-a1e608f470e1 | -12.48151 | -45.48174 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0088f14b-2e52-3abb-85bf-0a440e2fa84a | -8.22402 | -44.00426 | 2025-10-16 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 525330d1-349e-3d68-827a-68348b9cde57 | -12.31168 | -45.63363 | 2025-10-16 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 46d1ab1a-59a5-3299-890c-6e73c19d0b46 | -10.59843 | -47.43784 | 2025-10-16 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 4728badc-4f1b-3ab3-b156-2ec4e13b1fee | -7.11957 | -44.72649 | 2025-10-16 12:00:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 59cf5c4c-cd38-3573-a78a-4e9723b952c2 | -8.23027 | -43.32603 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 92e2a83d-278f-33c1-b26c-48f168bb1946 | -9.28608 | -45.37083 | 2025-10-16 12:00:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 9736fd37-1eeb-30b3-86a8-851bb49ff524 | -11.43329 | -44.1423 | 2025-10-16 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f649ef9d-ad5d-32f1-95dd-3637d76ed962 | -11.34986 | -47.2905 | 2025-10-16 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| eba5c71a-a1c5-3f93-bea0-d0328d6b4d7f | -6.50691 | -43.69496 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4d4a4c57-30b9-30a6-b234-4ae1c5c0076d | -7.41257 | -44.74693 | 2025-10-16 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 92a284e1-a140-3b36-8414-42f80fb51087 | -14.22004 | -41.89133 | 2025-10-16 12:00:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 7abca265-5bf6-3c95-bacf-777397a7f6e6 | -8.23647 | -44.79255 | 2025-10-16 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d60ac73c-6960-3c04-8a04-46d72915576e | -7.65595 | -37.62605 | 2025-10-16 12:00:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 46.8 |
| e9dcd76d-a503-3f6f-a052-0fa4c57ef9a3 | -10.13407 | -44.57212 | 2025-10-16 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 36d162ad-f437-3ee7-b60a-e53d06cd2c7e | -13.81677 | -43.34743 | 2025-10-16 12:00:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 57bba78f-b006-3db4-8402-05fdb510a648 | -7.4877 | -42.13752 | 2025-10-16 12:00:00 | TERRA_M-T | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| ac7ab3cc-f1be-3879-ac15-bdc8c831e980 | -10.13269 | -44.58143 | 2025-10-16 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 63c053c0-c73a-3dd1-9107-f35220d06504 | -6.42689 | -43.09937 | 2025-10-16 12:00:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 254.4 |
| 9864deee-b186-3463-a3ab-3fcf9576c2af | -11.42311 | -44.15004 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 218.6 |
| d3f395ee-ea1f-36e4-bcfa-0dd08c737388 | -13.50224 | -47.95966 | 2025-10-16 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2a9d4171-0358-38aa-9fdd-3ca54a580dbd | -12.94973 | -47.10564 | 2025-10-16 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| c0b89b88-073f-3129-b6f0-5b95fb506988 | -8.9865 | -41.18913 | 2025-10-16 12:00:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| cfb50e08-21e3-34c1-8e97-4eed044aa883 | -9.71907 | -44.50822 | 2025-10-16 12:00:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 7c9926f3-bdcb-38cb-82be-7a7c90f2cb62 | -11.47857 | -47.64091 | 2025-10-16 12:00:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ed7ec992-8036-388f-af3e-656a917dc892 | -10.65104 | -45.24935 | 2025-10-16 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ad4a1d74-acd8-3115-acff-5b48db4655fb | -8.86781 | -44.82944 | 2025-10-16 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 69d2b172-70a4-3a64-a356-cc9860a0191e | -11.35846 | -45.27979 | 2025-10-16 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| ebc79bef-14bc-3b5f-a940-d905f72af39d | -12.49067 | -45.48309 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7806a2fe-3840-371c-a062-de6139dcadb3 | -13.07208 | -46.98014 | 2025-10-16 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c22c9cb1-5e7e-3dde-b074-d84fc7775c76 | -9.2435 | -45.29568 | 2025-10-16 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 49.1 |
| a7f57f08-bd8a-3aaa-a33b-ed74a210ce11 | -10.60052 | -47.42467 | 2025-10-16 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 9fbf8076-9ade-3301-b5f1-34c95aebb5c0 | -12.27888 | -47.13179 | 2025-10-16 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| abf66ebb-62ea-3464-88a5-e42e9d420939 | -9.43912 | -41.38044 | 2025-10-16 12:00:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 86cba212-3b47-33ca-99d9-d1d6272ef614 | -14.06918 | -44.0387 | 2025-10-16 12:00:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 149953d8-32c9-3999-a045-3898a6882060 | -10.21817 | -45.1837 | 2025-10-16 12:00:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4a3ebc3b-5b4d-3876-8911-efad9a21c1f9 | -8.47786 | -46.24208 | 2025-10-16 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 3ac7a522-1c11-3bf9-9496-50a721b171f1 | -7.5718 | -42.58648 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| ee63c676-0a4c-3a66-93ff-fd8c038eebae | -8.38127 | -46.26952 | 2025-10-16 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| b2f1454a-94cd-3dac-abd0-b268525de807 | -13.40856 | -47.18917 | 2025-10-16 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 0fe58fd6-f89e-37d5-a715-8cacba0afea4 | -13.40677 | -47.20045 | 2025-10-16 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 61c2a0f5-0273-35a6-8701-7e3cab5fa819 | -8.29296 | -43.40512 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 19e329a4-0189-3112-b3df-35903b441ee2 | -8.30052 | -43.4153 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| 5daa8702-723b-3f9f-945f-f2cc3e551ef9 | -10.66065 | -45.31085 | 2025-10-16 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 44.3 |
| de80f64d-8d1e-3287-a331-b9fb47e41da5 | -6.59504 | -44.10087 | 2025-10-16 12:00:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 73c5516e-af31-386b-91de-efc9c2d21a1e | -10.65594 | -43.65209 | 2025-10-16 12:00:00 | TERRA_M-T | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| d0a7f6ce-3f31-3e2a-aaa0-4eaa4b527581 | -15.33509 | -45.03735 | 2025-10-16 12:00:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 244d597d-b4d4-3ecf-a0da-6779c9332438 | -11.4369 | -44.17977 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 451a752c-d5fa-3ab8-8e0c-96089ba158f6 | -7.89487 | -44.99182 | 2025-10-16 12:00:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0cf740f1-7791-3335-aa46-f1b98290db36 | -7.09734 | -44.25954 | 2025-10-16 12:00:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a2a7873b-1f5f-3946-b409-c5592ebece0f | -9.34647 | -46.93612 | 2025-10-16 12:00:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| daccd981-5366-3136-9295-5c64a22ca257 | -6.77919 | -44.66151 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c25d706c-f140-3c5c-be91-a02a09baba0e | -9.26227 | -45.27388 | 2025-10-16 12:00:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 283de2c8-eec4-36f6-9149-fc48669c4155 | -6.60322 | -43.91993 | 2025-10-16 12:00:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 62ab8708-7519-3e4d-82ac-8151b8866cfe | -8.46584 | -46.18625 | 2025-10-16 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 827dc895-852f-31fb-bbe6-c5799952e2f8 | -16.47905 | -41.56627 | 2025-10-16 12:00:00 | TERRA_M-T | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| 26c37f56-f803-3d50-b956-0e44a73dd9c4 | -11.42803 | -44.17846 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3033ce03-776b-3bdd-a998-2c1286c9f656 | -10.04649 | -39.65192 | 2025-10-16 12:00:00 | TERRA_M-T | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| e9bc95e0-74ac-3d8d-b845-8746f97518dc | -11.35074 | -45.26863 | 2025-10-16 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 6690fab9-7f2b-3778-8cc1-6b73d7269dae | -8.3951 | -46.24659 | 2025-10-16 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 7ab07c69-29b5-33a8-b894-276d522939ff | -13.06224 | -46.9785 | 2025-10-16 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a245cf24-4da3-3709-a733-09bdf84c2b65 | -8.06976 | -39.38241 | 2025-10-16 12:00:00 | TERRA_M-T | TERRA NOVA | PERNAMBUCO | Brasil | 2615201 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 6f021114-cf36-37d6-a859-a88c00adc55e | -7.28935 | -42.3119 | 2025-10-16 12:00:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 43756569-b73c-3028-a897-e6920bf176c1 | -9.18278 | -42.34749 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO LOURENÇO DO PIAUÍ | PIAUÍ | Brasil | 2210359 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 2cbb447d-75be-3efb-836e-b486ed40a9bf | -7.09592 | -44.26907 | 2025-10-16 12:00:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c85b67c2-990c-357b-b4d3-1f17b1158698 | -13.92243 | -43.50828 | 2025-10-16 12:00:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 63507fe7-3e2c-3a33-83c7-bc3608f78615 | -6.45201 | -43.37471 | 2025-10-16 12:00:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 91d7b7c8-3814-334e-bdd6-9e908d53eb61 | -8.46466 | -44.18967 | 2025-10-16 12:00:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4ca7f094-003e-3302-baed-22a88207dcdf | -7.85759 | -45.40438 | 2025-10-16 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 34259f89-eab1-3aff-9a32-8ebce4058e48 | -7.95353 | -44.15099 | 2025-10-16 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 416ad462-7a19-371a-b940-5f83091a90d3 | -13.77817 | -43.62033 | 2025-10-16 12:00:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5c9ee5f6-06d5-3f17-8a00-39952c111157 | -6.44178 | -43.3825 | 2025-10-16 12:00:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 023ec191-375b-3388-94a9-999ab9e7a5d4 | -12.28542 | -47.15165 | 2025-10-16 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| d4211339-9188-308e-a7dd-3ba99b3db50e | -6.56839 | -42.95958 | 2025-10-16 12:00:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9033b3eb-981a-3557-8268-865dc6ede371 | -9.35847 | -46.97084 | 2025-10-16 12:00:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| b75c4563-01c3-362d-a6aa-2a6d0200c1ec | -8.23911 | -43.32728 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| a5507972-975d-344d-a824-712e8b8c0f89 | -15.33374 | -45.04654 | 2025-10-16 12:00:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 26.9 |
| b16e6485-eec0-383c-b9ca-636ff7c3c3f3 | -8.25296 | -44.06144 | 2025-10-16 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 9683d167-cdde-3b58-9b43-037400e80bef | -13.52707 | -42.91516 | 2025-10-16 12:00:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |


[Clique aqui para ver as próximas entradas](README86.md)
