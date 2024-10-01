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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d568a8bc-2b7d-3dac-ab0d-b7f9b18a8d9e | -7.24488 | -42.25373 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ef712ec-be18-39f8-92af-0eee4293caf3 | -7.24209 | -42.24969 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d3eb835a-857c-3809-8884-ea231778739a | -7.24155 | -42.25321 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3cada422-5390-3719-bb9a-f46e80f09c73 | -6.98419 | -42.13729 | 2024-10-01 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6977f290-17f6-3646-9bb2-458b3e423a78 | -6.78917 | -42.2802 | 2024-10-01 04:12:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| ed49eed6-88dc-353a-8d5f-933c7bf317a3 | -6.65151 | -42.09714 | 2024-10-01 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5625f08e-5f9b-3432-9fe8-5ddf3a47d2f0 | -6.64873 | -42.09312 | 2024-10-01 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e6f2d6e0-70d4-387f-ad5d-b69d60de1a13 | -6.64151 | -42.09562 | 2024-10-01 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f00ecb04-3561-3fca-9edf-8070457cc5b4 | -6.64096 | -42.09911 | 2024-10-01 04:12:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 70db3776-31fb-3284-9dda-103ca87fa30e | -6.64042 | -42.10261 | 2024-10-01 04:12:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fddfea9b-677a-371c-99c9-04f42c2b0aae | -6.63763 | -42.09862 | 2024-10-01 04:12:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3fe813d7-6577-3adb-9286-1f8e42918e25 | -6.63708 | -42.10212 | 2024-10-01 04:12:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c2f4e4d7-1263-3343-b158-f967ff2b9c88 | -7.87527 | -42.67545 | 2024-10-01 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a60eacd0-6bc1-33dd-ac0e-f4bf63785ed8 | -7.87473 | -42.67895 | 2024-10-01 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9ad1459c-0789-3abc-95bf-3e1f428e19ea | -9.27102 | -43.45972 | 2024-10-01 04:12:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 076a3bd0-aedd-364f-bcd3-0124df5f8533 | -9.26687 | -43.46228 | 2024-10-01 04:12:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d3b2739f-81bf-3663-adc6-1a601bd15c40 | -8.31504 | -43.38247 | 2024-10-01 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b3bfe5d8-32b0-393c-b901-ca75dc4b053c | -8.15482 | -42.9084 | 2024-10-01 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fff77d75-b125-30e4-b049-89d4787b06b4 | -8.078 | -42.87859 | 2024-10-01 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f3f89c15-fbdd-32a2-997d-0584c494f07e | -8.17863 | -43.66661 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3802f8fb-0fca-3738-98ee-bcf99dae01f6 | -8.17587 | -43.66261 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2881e867-0278-3faf-a43d-a75778c9136c | -8.17478 | -43.66955 | 2024-10-01 04:12:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a996734-b500-3518-9a53-95c73dffb4a2 | -9.942 | -44.03053 | 2024-10-01 04:12:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1e9599b-d83e-379a-a42e-33eede54e7e9 | -9.94145 | -44.03402 | 2024-10-01 04:12:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d815081-f85d-3d6e-8aeb-b2212c46ba23 | -9.93751 | -44.03701 | 2024-10-01 04:12:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a978666-48a2-3633-a00a-49fde5d87d88 | -9.9342 | -44.03648 | 2024-10-01 04:12:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 808c594b-e229-3495-b638-44d7c3e99444 | -9.92043 | -44.08078 | 2024-10-01 04:12:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f316cf5-543c-3f34-935e-d0b371159063 | -9.91712 | -44.08025 | 2024-10-01 04:12:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3672943e-9ddf-3742-9d39-1983825a262a | -9.91051 | -44.07919 | 2024-10-01 04:12:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20118aec-1805-3fde-8d40-201d9593912f | -9.9083 | -44.07167 | 2024-10-01 04:12:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b02b58d-b80a-3e4e-893b-745000bcb9aa | -9.90775 | -44.07516 | 2024-10-01 04:12:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd987536-5205-332a-a9fa-616aa67c05aa | -9.90499 | -44.04967 | 2024-10-01 04:12:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 480ce66f-9584-30f3-8935-e13252df18da | -9.90168 | -44.04914 | 2024-10-01 04:12:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6bef145d-2013-3dd4-9d10-3cf488326b27 | -9.89782 | -44.05209 | 2024-10-01 04:12:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1ef02b5-7ebf-3c9d-8e08-d2d20e442372 | -9.48535 | -44.06095 | 2024-10-01 04:12:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3653e23-f2a2-348a-aa19-387a5b8382f4 | -9.48204 | -44.06042 | 2024-10-01 04:12:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cce0670-7e11-37eb-8429-cc2f34bc3232 | -9.48149 | -44.06391 | 2024-10-01 04:12:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 820b0904-f6a8-3fc4-8efd-1a5aa6096f63 | -9.47818 | -44.06339 | 2024-10-01 04:12:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcd033f9-c7d8-3207-aa5e-d33af40e2c1b | -9.47762 | -44.06688 | 2024-10-01 04:12:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16939349-e864-3e6f-a752-bd12cd900983 | -9.47432 | -44.06636 | 2024-10-01 04:12:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a86f574-b84a-3a3b-8fdb-ef9bf2675364 | -10.47421 | -43.64713 | 2024-10-01 04:12:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df7a9032-3d49-320d-918b-12784624675d | -10.24171 | -43.59242 | 2024-10-01 04:12:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9877a67a-793f-360b-8224-8e8df4307597 | -10.2384 | -43.59189 | 2024-10-01 04:12:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8b58e41d-3143-3f6f-ad15-b06b6d645346 | -4.81726 | -44.35623 | 2024-10-01 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b52f2334-2600-39b5-bd00-4fdcede079bd | -6.5059 | -43.63176 | 2024-10-01 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cca9d358-f306-36bb-8015-00a2306a6980 | -6.50259 | -43.63123 | 2024-10-01 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81e13ab4-d05a-3ea8-98d5-d4c725b2b0f6 | -6.50204 | -43.6347 | 2024-10-01 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c62f3f23-59dd-32ec-9181-5ac0d1a7dbce | -6.35118 | -43.92247 | 2024-10-01 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 33bb39b1-a723-3444-8249-edf8fc4ad7b3 | -6.34784 | -43.92195 | 2024-10-01 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c158785-ceb3-327d-8308-6c732be4fe3d | -5.97013 | -43.62527 | 2024-10-01 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 555ffe30-0b05-3bd9-bea7-759e16799fbb | -5.96958 | -43.62875 | 2024-10-01 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64ecd629-9842-336a-b191-54759355c633 | -5.88703 | -43.7196 | 2024-10-01 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4312848b-e410-351c-bf65-3c81a80e8aed | -5.88647 | -43.7231 | 2024-10-01 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e305314-092f-3b4a-a062-bd22d51e6836 | -5.88426 | -43.71556 | 2024-10-01 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84a44b51-72a6-35f3-b650-16c9d47317bb | -5.8837 | -43.71907 | 2024-10-01 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5078447-54b3-31b7-84d0-9236c8631557 | -5.40552 | -43.43609 | 2024-10-01 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 76014663-3653-365c-ab3a-ed2dc69392f6 | -5.40497 | -43.43957 | 2024-10-01 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7c17ff5d-343b-329d-aca3-d4e34e2a06e2 | -6.46307 | -44.02708 | 2024-10-01 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee462974-3169-3426-9aef-d9f376a2416d | -6.25009 | -44.14888 | 2024-10-01 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 041b953a-a9be-3404-96d9-940c4e639a1a | -6.24952 | -44.15244 | 2024-10-01 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03bd2fd5-67aa-3461-8865-9fda0428dace | -6.24731 | -44.14479 | 2024-10-01 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1042779e-5f62-3f75-b35e-b32d3c497932 | -6.24674 | -44.14835 | 2024-10-01 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 35d2ab83-7f8c-343e-a8ac-025ae4ac5dc9 | -6.24617 | -44.15192 | 2024-10-01 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d08e89b7-da17-3bb6-a257-3431367b1ee0 | -6.24452 | -44.14072 | 2024-10-01 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ac391fd8-3ab9-3dcd-9814-1ebac0047431 | -6.24396 | -44.14427 | 2024-10-01 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fc9421a9-d718-3b7e-8fa9-2529d648ffb9 | -6.24174 | -44.13668 | 2024-10-01 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 84149007-5164-38a5-bbd0-10c2e4ef8596 | -6.24117 | -44.14021 | 2024-10-01 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1028c576-4d69-3fdb-b21b-2f3f20d2a930 | -6.38737 | -44.77812 | 2024-10-01 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dfc35a9-4959-3800-aefc-45889c086c85 | -6.10064 | -44.70697 | 2024-10-01 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33503576-875d-37a9-8da5-80ce90e1f2cf | -6.09724 | -44.70642 | 2024-10-01 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e62c6d0-e6c0-3b80-b043-ad79f5ac9a9c | -6.09192 | -44.30715 | 2024-10-01 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5d320c9-dccb-3241-ab46-e7c584caee31 | -6.09004 | -44.30738 | 2024-10-01 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f86ba932-de73-3b93-a80b-85829730c859 | -6.08667 | -44.30685 | 2024-10-01 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ec8230a-cf0e-39b4-829a-e3da2683488c | -5.32013 | -44.47958 | 2024-10-01 04:12:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92a27d14-b006-3a1f-a17b-eeafe28842c1 | -6.69041 | -43.92649 | 2024-10-01 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01e584d8-812b-306b-b6c4-4f7970e7b6b7 | -6.59562 | -44.17884 | 2024-10-01 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2918485-7a67-31b4-85b1-2f19fd82ffc1 | -6.59341 | -44.17119 | 2024-10-01 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc4e1a2a-bdd8-36ec-bf4d-40e2fb47daaf | -6.59171 | -44.18184 | 2024-10-01 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c4b8b70-013f-3d0b-9082-d35c4049e92b | -6.59006 | -44.17064 | 2024-10-01 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09b82d93-9f34-35b5-a04f-2f769f4bc216 | -7.29722 | -44.96718 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64ae6e05-c029-32ab-ae09-128296c43384 | -7.29662 | -44.97084 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72e629a9-4f20-3dd3-beb0-4d948a7160c5 | -7.29543 | -44.97818 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ea8f145-2d7b-3b85-a1ef-ee34e07f4b9a | -7.29202 | -44.97764 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 191b14e8-4a2a-3164-a7a4-0d6c23da6ec0 | -7.28485 | -44.9315 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ed79ce2-8b0c-3c28-b2ca-2a363cf66086 | -7.24983 | -44.9977 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aaeedaf4-b4f8-3e14-8ff2-0231772f36f2 | -7.24643 | -44.99714 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d31710b-1369-3371-8d67-c93667b00415 | -7.24243 | -45.00026 | 2024-10-01 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ab989e4-28d1-3f4e-80e9-705f46e8060a | -7.09663 | -44.46664 | 2024-10-01 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d0abc39-561d-372d-bf8e-35ef8f88c65e | -7.09015 | -44.55029 | 2024-10-01 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98c0a586-9eed-300d-8bc8-4fc06d2d47aa | -6.69175 | -44.53856 | 2024-10-01 04:12:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49d1d495-da7b-3a15-8ff6-51ceb72e5a68 | -6.68837 | -44.538 | 2024-10-01 04:12:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b464873-6de4-38af-b67f-211a2d4e2285 | -6.62195 | -44.64997 | 2024-10-01 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b1f0f40-4dba-3d5b-991e-1846edfeeed1 | -6.61858 | -44.64938 | 2024-10-01 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b06e44f-3aed-36fe-bcf6-79898840a950 | -6.58256 | -44.63589 | 2024-10-01 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35d220ee-465c-38a4-b4df-9ffa7dda8503 | -6.5696 | -44.62361 | 2024-10-01 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 120f1c31-85ec-3185-8bdd-762e7843072d | -6.53407 | -44.49905 | 2024-10-01 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 289756d3-8264-34f8-aca0-aa1bb88e4ffa | -6.53069 | -44.49852 | 2024-10-01 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5951dad2-864d-3c86-bff8-373fc664d6dd | -7.60045 | -43.86304 | 2024-10-01 04:12:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78ad03e0-6c57-3588-a8ed-1ed5d847edf2 | -7.5988 | -43.85203 | 2024-10-01 04:12:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42d988bf-8d15-33ff-af6e-615fc4bab46d | -7.59713 | -43.86252 | 2024-10-01 04:12:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README69.md)
