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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ba726ba-713b-364a-86df-06d8f7098920 | -11.90644 | -47.89133 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e0fd773-4133-3a0b-8e82-ff8a9873d6a7 | -12.67441 | -48.57032 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95625369-d500-3989-840a-5d7c8485165f | -14.36717 | -45.96154 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b47e4869-4c7e-33ee-a2db-ae4d77827f48 | -14.98604 | -46.90746 | 2025-10-02 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 69e92c6f-4c4a-3dd5-8e37-8ed4c35730fe | -15.32889 | -46.29424 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3457b231-3256-31cf-9e11-179002567e39 | -11.80971 | -45.00682 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d07b4f5a-ac92-3e95-8c71-29666d90417c | -11.46891 | -45.00123 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a99b717-375d-32ba-97dd-73d7412a12f5 | -9.79628 | -48.57193 | 2025-10-02 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8f0b154-3c80-3486-b984-e84826ea6a81 | -13.75797 | -47.9561 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4a6c61b-4307-3369-bf49-69d1ae2847fb | -16.01993 | -50.8656 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b56ad2c1-d078-334d-9957-1a91bce688d4 | -11.44211 | -43.89732 | 2025-10-02 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3bb2bb3-387b-3ce8-89f4-82c8ff1cabcc | -14.48985 | -48.42781 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 857f7f9f-4798-3747-9ac9-9ba529cfb9b5 | -13.21529 | -47.35315 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d877213-69c7-3ea6-8691-7ea4f410b819 | -16.1029 | -51.04314 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 418b648c-38ff-3d74-bbe9-b35b41aa23ef | -13.08668 | -47.08154 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d8ecd54-f727-310f-aecb-9d1b982b791e | -11.26787 | -47.80397 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0843df38-c12e-3a34-ab35-058c71ec1491 | -14.32151 | -45.88012 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc0c5e52-83f8-3c78-b2dd-87326132697d | -9.81325 | -48.2608 | 2025-10-02 04:51:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84c54185-cc9b-34c1-be04-265e05af50bb | -13.21456 | -48.49845 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a359c0b-52ea-3bbc-88b4-70f0221e0baf | -11.26261 | -47.81081 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4c4fd11-a6a5-34b7-88a5-67e85dc459a5 | -9.8056 | -47.84527 | 2025-10-02 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc637cd7-8fd7-3342-bb4b-c257eab51574 | -11.46543 | -45.02917 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5998201a-46d9-3f10-8142-009c7f09da3e | -11.47122 | -44.98274 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87419a9f-53e6-38d3-9ab9-a622c54e2e69 | -11.80354 | -44.97209 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d3830a7-dc36-3e6e-9f7b-dc7746560845 | -14.30098 | -45.96332 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d2b01339-8347-3c02-b10b-b987aac57ef9 | -13.80574 | -47.535 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b98df5dd-9b1a-38ae-9b21-00b829e82068 | -17.07535 | -44.91104 | 2025-10-02 04:51:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2eaf5604-ac3c-34f2-b81e-d53a7af30f59 | -11.53325 | -46.95589 | 2025-10-02 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 974f28de-b9ac-35d0-b2bb-fab3b7fca0e1 | -9.49267 | -63.13543 | 2025-10-02 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa57d406-179c-3b00-b774-72301b51c6e9 | -11.42806 | -43.49896 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 443fa37c-c9be-31f6-b1a9-9935a48afa7e | -16.05166 | -51.03139 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 489e1ac1-1597-3ae4-8bf3-9936e1aa1eb6 | -13.20807 | -47.33824 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74c919a4-8ac0-3a88-894f-2e674272fc43 | -13.34363 | -47.33132 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b3b2b71a-f0e6-3684-bfed-c2bfd5fe6113 | -12.90268 | -47.17236 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e60709c-e9b0-3db1-96da-5b88f3ccbcc3 | -9.92754 | -50.49333 | 2025-10-02 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b5a48ffe-2135-304d-87e3-0054b2bd1e3e | -13.74542 | -48.71014 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f13ebad-90b2-3954-8a3b-42d493f20c95 | -10.85709 | -45.4143 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e194c16f-761f-389d-aeaf-0754d760c37b | -13.21241 | -48.51422 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 392f7613-8a87-3595-a21a-ff7e10aa1446 | -13.65015 | -47.65987 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f04703d-d4bd-31a8-b452-e989ae2256c4 | -15.94393 | -43.33009 | 2025-10-02 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26432344-2381-38e0-ba7e-ac6708a3b01c | -13.78395 | -48.0058 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d37cc6a-7e58-3af5-b82e-f2f6de1fa7ec | -10.99546 | -46.58804 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85f2ac02-6826-36a9-bd14-f3e5858a02c1 | -13.95581 | -48.10059 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 791f0949-6675-398e-9e33-ca3a958252a3 | -12.86171 | -47.01828 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a683dfff-86ba-346b-ab13-5289d98e2760 | -11.18113 | -47.26418 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6a75ee7d-4d66-3b55-82d0-c361fc6a2886 | -12.70513 | -48.58996 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4c863f6e-bd6f-3455-bf0e-8c10d14b3a32 | -13.17897 | -47.83638 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43923db8-c242-322c-8943-4e8c5bdfb4ae | -14.58447 | -48.32728 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 105930e7-8232-3c94-833d-271abbcbecdc | -13.95644 | -48.11122 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c1118a2e-6be0-302c-aef5-65eaac6b0d6a | -9.94863 | -48.78903 | 2025-10-02 04:51:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b55b5a4-493a-37ff-bca1-eb9589e788df | -10.83254 | -46.61943 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 155259cb-6d45-33db-aa8e-e3c6a6ee9bc6 | -10.82567 | -46.63156 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 29a41f41-6191-3db1-990e-5e0ddd435c73 | -11.09105 | -49.69602 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abbf22d3-5142-31aa-a38f-b89cbf7eda7f | -14.31107 | -46.00587 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0f8f1a48-bead-3e13-9940-242d1861dbda | -11.07818 | -47.80415 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 566d8800-dbe8-39e5-816d-6ffae27d9835 | -13.95208 | -48.12952 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 191b881e-e45f-3650-b4af-a5f44dfaa462 | -11.45051 | -44.96534 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb6e59df-3d07-3559-abc7-690975a11c78 | -13.52064 | -47.25753 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e3390f6d-d37f-3172-b967-02341f1520b8 | -10.22611 | -48.22031 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57e74aab-6f16-3ba5-8e87-db9098951f6b | -10.82159 | -46.63204 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d36949ba-17ea-31df-b1e5-55460e8b047a | -14.41141 | -46.09637 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 14a11f51-463f-342a-afe9-3156ee4c1807 | -14.58128 | -48.31813 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e82702f5-7798-36c7-bbd3-26a7c6d1b26d | -9.40287 | -47.33362 | 2025-10-02 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7bf93537-b229-39c0-9773-e46cadeb391a | -13.31718 | -47.20704 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e510a9b-8f32-3d09-b3aa-64f6854a2721 | -13.13134 | -47.41703 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e1c9076-10fb-3e46-b961-e1bba17ea4f5 | -15.25783 | -49.28716 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf770f18-70cd-3da0-9820-d591b879c26d | -14.37649 | -45.96869 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0316fb1c-6b6f-3c99-84b7-e26a57a489a1 | -10.06483 | -48.18895 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06a86e3d-3dcd-3246-8a3d-22623518916f | -11.01089 | -49.58315 | 2025-10-02 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b8cb596-744a-3560-9c61-056e376c1dec | -14.47078 | -48.40797 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 023b1bca-6e4b-3058-a75b-937f9098cc4d | -14.98036 | -46.86735 | 2025-10-02 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6238c2f9-ae7d-3543-8713-d4ec540c4599 | -14.65497 | -48.12243 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c7a6361-2cd6-3089-83b1-9e92e8ff28e0 | -15.10483 | -48.37168 | 2025-10-02 04:51:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7b4d5ee-af31-31da-b2a3-0693c73a91db | -11.19545 | -47.19064 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e41af248-6f6c-32d5-885c-d4f9c6c73353 | -13.81408 | -47.54065 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dacca4cc-8154-37ea-81ec-3b4029448e98 | -11.57834 | -50.1699 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 13b47039-3c5f-316d-b0ed-64381c5d6742 | -14.88429 | -48.31404 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa07fb1d-614c-3942-bee2-df79ac32e31f | -9.93145 | -43.73716 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 40.0 |
| 50b08157-8cbb-36f4-90de-053a2f236038 | -10.66929 | -48.52653 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1feaa683-9fe7-3d8e-8147-8153fce93969 | -11.81369 | -45.01693 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1308b17-9549-3531-bb79-216d49cfeba1 | -15.27531 | -49.3108 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 381dee43-40ef-34d2-a006-ea3798e446e0 | -11.60873 | -45.03083 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e63f8b26-c859-3950-b1b9-93bf21995636 | -13.87003 | -47.95658 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b33a5ed6-d619-340e-8198-94e6c588e7a1 | -14.32115 | -45.88303 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ef8b907-97c7-30df-b9d5-8f9dade44cf8 | -13.76261 | -48.00054 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d263ec5-7940-3c6a-9013-d6248043f3d0 | -11.81837 | -47.68476 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2488a900-1055-327f-863c-78b4cbdb3ab8 | -15.22501 | -50.11757 | 2025-10-02 04:51:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74a11424-7124-398a-81be-0f22efd36b7b | -12.43261 | -50.16871 | 2025-10-02 04:51:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08097b38-a7ec-3c2d-b8ed-def0e5e30c8b | -13.23477 | -48.50547 | 2025-10-02 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cdcb00a-1cca-3053-9b60-d32cd47784cd | -11.61841 | -45.03692 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc2adf35-17d1-30ba-852a-0732c04a177b | -14.36613 | -45.97015 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b95d1fa-9885-3426-8475-23254eaf788d | -14.42267 | -46.12706 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53c3002d-1ba2-315b-be28-f58944aefa34 | -14.21806 | -44.93927 | 2025-10-02 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05aad2d0-c7b6-3fe0-b611-2c87158b3937 | -12.50194 | -50.25389 | 2025-10-02 04:51:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0405029d-f371-38d4-a820-1375fa56f590 | -15.17499 | -52.80938 | 2025-10-02 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 21aa3bec-5177-3185-a0b0-0429dc58e3ec | -14.62263 | -48.30234 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 012fd692-548d-35c1-92b9-8f5317253618 | -14.58585 | -46.71922 | 2025-10-02 04:51:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2c2bc7e6-23d9-3ac3-b190-d7d6485cb055 | -10.22357 | -48.20902 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3a32fd7-5e97-3ba9-bdca-a6847b92bf4e | -12.2629 | -47.80625 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 91bdb0b2-27c8-3faa-8fff-9866846863cc | -13.32052 | -47.33286 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README126.md)
