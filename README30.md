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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 620e080e-2de6-3b6c-a365-f46802e79927 | -10.90705 | -44.8421 | 2025-11-18 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7aa89110-d6ea-3263-8b3e-077185964eef | -6.4434 | -45.73607 | 2025-11-18 04:21:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbb46fd9-4cd6-37a8-ae91-3640baeefedd | -3.38498 | -51.02277 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4248fc34-8623-35ed-99f7-8c3963aea831 | -6.44006 | -45.73553 | 2025-11-18 04:21:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5680521-9449-3356-adc6-46196be47744 | -4.19221 | -44.23832 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e255144a-f05c-3add-a447-e2d6456e3109 | -6.86437 | -47.07685 | 2025-11-18 04:21:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77a2b450-10f9-39e3-9e2f-40825275191c | -6.49703 | -46.39426 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b2161f1-b7f6-391f-9186-bccc0a9b8a60 | -8.38909 | -44.06373 | 2025-11-18 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c017f353-070f-33f6-a8e0-3472b17cce59 | -9.3997 | -48.44511 | 2025-11-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 00af185c-30ba-3507-90be-ab0790bae25a | -6.2171 | -46.88515 | 2025-11-18 04:21:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fc1d085-26bd-37f9-bcd8-cbcdeec3da07 | -7.96215 | -35.24741 | 2025-11-18 04:21:00 | NOAA-21 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2d8683db-dc42-3a37-a031-f40c84475481 | -11.40002 | -43.31744 | 2025-11-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48e7b0d5-b0c8-3ac7-b65a-878661686dba | -3.68589 | -50.54195 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f60c958-9e17-3a04-8b88-b7d17b77a927 | -4.7087 | -46.30779 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e046004a-04f7-36d0-8cdc-f9f716f47e7f | -7.43833 | -45.18859 | 2025-11-18 04:21:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68a89692-634e-338d-a517-ac82876d76fe | -4.61752 | -47.25593 | 2025-11-18 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f0010df8-b515-3205-9737-a6c949c98427 | -5.40696 | -44.06358 | 2025-11-18 04:21:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f9f12112-d6bb-38f5-a407-7c6ab4212bb4 | -3.88111 | -47.18903 | 2025-11-18 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b62d217-04e9-3097-bcf4-3d698e21e221 | -4.179 | -44.23627 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8a5ed590-ac31-3418-95eb-1822b59c6a2a | -10.91418 | -48.67594 | 2025-11-18 04:21:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ea7f1c7-8905-39d7-a401-52d54d4943b3 | -11.39538 | -43.32472 | 2025-11-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 222fcf33-f2da-366a-b5d9-b0fef61d39a6 | -5.46695 | -40.96912 | 2025-11-18 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fc54bbcc-b2a0-3653-9152-363c06790c85 | -5.74426 | -46.28722 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2d4fb13-fe52-3492-a872-43818bfc4aaf | -10.34722 | -48.91521 | 2025-11-18 04:21:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36ae61cf-70a3-301f-ae13-b8a5b077d03c | -8.30469 | -42.25944 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 73f3f5bc-164e-325d-9c33-f33b9d976484 | -4.13304 | -46.36998 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b55f932c-8389-31db-90e2-82c819214914 | -5.38038 | -50.48474 | 2025-11-18 04:21:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30281e16-82d7-3da9-9849-f7bc728a508d | -4.16391 | -46.8325 | 2025-11-18 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c13e7e02-a2dd-3aa2-ad15-e50aae0dcd02 | -8.29315 | -43.95814 | 2025-11-18 04:21:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f67550fa-2ded-3aec-815b-a75ebb0f466f | -8.21422 | -48.30351 | 2025-11-18 04:21:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08355ef5-36fd-3487-8c75-a149cdd2a4e0 | -7.35817 | -46.21149 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 554091a4-edfb-353f-b15d-4cf4a02b040e | -7.54389 | -47.04705 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5564fd61-156a-3266-b836-f43f94fd659c | -10.35234 | -48.92926 | 2025-11-18 04:21:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0391d9d-2395-3866-9f05-10858d8db095 | -10.87821 | -49.54507 | 2025-11-18 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d014d734-7238-3690-ad4b-025c578a0f02 | -4.71593 | -50.95048 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ded4ea7c-569e-3829-92e4-c2ae73b9b6a9 | -7.9278 | -46.03152 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4141e76-f806-3a4e-a5fa-003de145af05 | -8.77835 | -48.45971 | 2025-11-18 04:21:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9496a3a-f578-3bb1-95f3-1c8768fda190 | -10.35744 | -48.92129 | 2025-11-18 04:21:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 21962192-328f-3d69-94fa-a16c77674d50 | -6.88082 | -44.60016 | 2025-11-18 04:21:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 758dab1a-3a83-35d2-9629-e8ef7100eded | -6.67285 | -42.03899 | 2025-11-18 04:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| c7f345ac-45b5-3155-9b25-2eceffb967a9 | -7.13538 | -41.65398 | 2025-11-18 04:21:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4a19e229-4a9b-34d4-bd37-bd9bb78425a2 | -9.39472 | -48.45292 | 2025-11-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 723f7d2c-8114-3b70-9acb-b02fe6120600 | -4.38276 | -46.03983 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 686b6e5e-78c7-3509-8dec-58c7cab79c11 | -6.37024 | -42.32242 | 2025-11-18 04:21:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 74019308-145f-3380-9d6e-4d89716bc4c4 | -7.62133 | -42.58463 | 2025-11-18 04:21:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 233dcb0b-36b2-3c97-b4e3-72043c26e798 | -7.80109 | -42.62206 | 2025-11-18 04:21:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 643dc8a3-a500-3a6c-b6a0-0f18bf8f9804 | -6.84016 | -46.27249 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b98c7cf0-c4f4-35c9-8d2a-45ac695f88f9 | -5.35981 | -44.90739 | 2025-11-18 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3fc9e4b-847e-3d83-bdc3-a40bf862c35d | -7.16858 | -40.65749 | 2025-11-18 04:21:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 95d610db-a449-3b47-a29a-6b9ad5f1d3c9 | -5.88595 | -43.9795 | 2025-11-18 04:21:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e241a8e-5d16-3b31-83ac-de5f3fe8e98a | -8.57251 | -45.52731 | 2025-11-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e5626ef-2874-3f90-a6e3-f0868b0d3f25 | -5.51826 | -49.56279 | 2025-11-18 04:21:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b3800a7-fab0-39bf-bc76-2a1a75a6e117 | -8.20985 | -45.04254 | 2025-11-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eb2344f9-dfac-353d-8b97-932c0f1c696e | -6.54948 | -46.63416 | 2025-11-18 04:21:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdfc2ae1-d240-3d62-9294-b71a3788bcfe | -7.43669 | -45.19901 | 2025-11-18 04:21:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7acab76f-eedc-3fc6-8b9a-71e5cc1b6ccd | -4.27577 | -44.24847 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b600811a-cf95-36ec-9a60-b3593196d928 | -9.3961 | -48.44453 | 2025-11-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c5e4f9f2-9ee7-30c3-9d78-ced80c42de10 | -8.55364 | -47.78054 | 2025-11-18 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 895c97c7-1d50-3476-be15-26096ce5fce9 | -9.40982 | -48.45107 | 2025-11-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eeaf5a80-913b-344f-8a89-3fb74e9ec13b | -7.33701 | -46.17127 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8a2ba7e2-3fdb-35a1-8c07-c82d5dda210d | -6.36603 | -46.15694 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca32c74e-8256-3aa3-b38f-f9594270c41b | -5.83637 | -44.68953 | 2025-11-18 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9ebd541-64f3-3d3c-8e47-a6ad94c0153b | -6.31163 | -43.7797 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6bfdf9ec-9e79-378a-b13b-e1d020d0ed53 | -4.76844 | -44.92439 | 2025-11-18 04:21:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 487e044e-98f2-330c-b7e5-a32503eb2d1d | -10.17638 | -44.66518 | 2025-11-18 04:21:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1dd19a33-a5d3-3f11-9414-8cfda8a84100 | -3.46576 | -50.1211 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c54830b-6548-34b1-935e-8d0e594745ac | -8.8655 | -47.32328 | 2025-11-18 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98e1e180-9b73-3c95-9bb8-6230937e6b03 | -7.80051 | -42.62587 | 2025-11-18 04:21:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 72c7deaf-7bc9-314e-808a-b6a2f65cf638 | -7.20225 | -44.63345 | 2025-11-18 04:21:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa3e2f95-b44e-38e7-9e52-39b09e626dd2 | -5.83307 | -44.68901 | 2025-11-18 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cfe8d7f-bedc-385e-ac6a-bc5390108d00 | -4.13956 | -46.35149 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e3b78e8c-3697-3deb-96d3-813fe1707d7f | -3.24163 | -50.49509 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcdcdca4-2352-363e-8e21-e69c90522cb5 | -4.70525 | -46.30727 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9009e4a1-400a-3119-b53f-99e4c1df448b | -4.22875 | -46.34206 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c243e727-e6c2-343e-9310-83e70e890ee5 | -4.78286 | -45.626 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c470ccb-0648-3943-a4c4-a4084d6c26ae | -6.87639 | -39.84621 | 2025-11-18 04:21:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dc3e68ec-d5ef-36f9-b57b-555dd47b8884 | -5.45774 | -40.9806 | 2025-11-18 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a5888bb6-4d58-36b3-abb1-28488c15ba4f | -7.62479 | -42.58516 | 2025-11-18 04:21:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e7da9400-0038-31d5-8bc2-b09d6066e14f | -7.85667 | -46.87263 | 2025-11-18 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 187a027e-2ac4-3241-bffa-4d47b507005d | -5.56018 | -47.10654 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9cdc188-3343-3098-a826-b8054bedce94 | -5.13177 | -46.23241 | 2025-11-18 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12fe83ca-cda4-3891-877e-a7db569dd747 | -10.33647 | -49.63887 | 2025-11-18 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0580a513-ae13-3456-a227-809b41b24934 | -4.97312 | -44.68322 | 2025-11-18 04:21:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1833093c-36ce-3584-8c98-bff8b0fbf191 | -10.58651 | -49.01104 | 2025-11-18 04:21:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3a7ec00-b831-3831-b197-4cebb5030e2e | -10.35306 | -48.92499 | 2025-11-18 04:21:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d491020-830a-32b7-a0b3-ddb4d4884f7b | -10.51551 | -43.95757 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da26ce9b-b99f-313a-bd21-bae59e351adf | -9.8072 | -41.71904 | 2025-11-18 04:21:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9d632086-dedb-3f02-a968-056eacbfb4d9 | -10.51496 | -43.96124 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cf46cd9-4180-3bfa-bb1d-45a524720268 | -3.08887 | -51.26083 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46a5958c-39d7-3208-9306-90edb080c488 | -3.25556 | -50.69216 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 511e45a7-144c-315c-9dc0-0f3ee7684125 | -3.23195 | -50.49795 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06cfc469-bcc5-3ab0-8203-cfdd0903ff79 | -10.29365 | -43.98733 | 2025-11-18 04:21:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd4bbdc9-c213-3fe4-9a95-b41e33a0191c | -10.76663 | -44.17863 | 2025-11-18 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e959ef2f-be2f-3487-8225-ac40fc53de6f | -5.62847 | -44.95018 | 2025-11-18 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05e629dd-9623-3a05-8e24-20bf5df32e50 | -7.5176 | -43.05655 | 2025-11-18 04:21:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4cd60364-bd37-3694-9533-3cc3185816d1 | -8.58603 | -44.11217 | 2025-11-18 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dce2d539-d10d-3af3-bfec-71ef7413dd8d | -10.44816 | -49.48825 | 2025-11-18 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5df72cc2-27f5-38c5-a238-6b0fa2f62b77 | -9.44821 | -45.58292 | 2025-11-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a10326c-fb0d-383e-8fda-0f4cf1d78fc7 | -6.93608 | -41.53426 | 2025-11-18 04:21:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8b070803-4a27-3002-8bf3-7eb5945ffdf2 | -5.90392 | -39.88968 | 2025-11-18 04:21:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README31.md)
