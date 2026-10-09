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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d756f85-53f8-3a85-8df4-dd7a38dce80c | -5.6952 | -53.504601 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3f83e1b-adcd-3c8e-8a8a-4fda10151f90 | -7.4748 | -42.865101 | 2026-10-09 00:28:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 36f09827-eba8-36d9-8c4f-9dd463761885 | -10.2729 | -47.8232 | 2026-10-09 00:28:00 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7838d2b4-1fe4-3d85-8b61-a3a369d1a839 | -7.2933 | -45.415901 | 2026-10-09 00:28:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d184558b-06b3-36c7-b498-707faf2259e4 | -7.4809 | -42.847 | 2026-10-09 00:28:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6c91d86a-f277-3944-8309-32d76cb07de6 | -18.3281 | -42.379601 | 2026-10-09 00:28:00 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fa7f6dc6-bd27-3c71-92bc-0c4bd412dd3c | -9.9122 | -44.7831 | 2026-10-09 00:28:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4800d97e-3070-3d15-ab75-7b1aa4912b6f | -3.3557 | -50.4832 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe8a789e-a30a-3abd-bec7-ac6d5dcf55bc | -3.0769 | -53.938099 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dba45789-9409-34b0-a457-0592a7c0cf11 | -3.5455 | -54.665798 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eccca81-eced-3162-8cfb-dd08ff083bf3 | -7.2063 | -55.157501 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7e9edc8-4c71-3ba6-9a92-a0818cbcd483 | -5.4867 | -44.294201 | 2026-10-09 00:28:00 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| becacbaa-1851-35f0-8098-696a527165df | -19.086201 | -43.991001 | 2026-10-09 00:28:00 | METOP-C | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 22f5b59d-d737-3e5f-9d20-1769ef5dd183 | -5.7573 | -43.8606 | 2026-10-09 00:28:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b5810c00-2640-3328-bc57-4f64280afd39 | -2.4601 | -56.094398 | 2026-10-09 00:28:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 671a2f1f-3af1-3680-9401-8e63b0b34952 | -5.8408 | -44.931499 | 2026-10-09 00:28:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f9b286d-f048-35b7-b1f0-11c4490e735c | -2.9559 | -49.173599 | 2026-10-09 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71887781-9d05-3095-b292-532c80327fac | -4.147 | -44.345501 | 2026-10-09 00:28:00 | METOP-C | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aabed25c-48d7-38af-869a-f870f54719b3 | -13.527 | -44.404499 | 2026-10-09 00:28:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3d118bb8-a037-3884-b80d-a348cc7a263d | -10.874 | -44.795799 | 2026-10-09 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31265f0d-073a-3898-aa30-d93c40d37050 | -11.1164 | -44.006901 | 2026-10-09 00:28:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b70ca5d-705a-3da4-a1a6-88c9f594144f | -8.2195 | -46.405701 | 2026-10-09 00:28:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e27b84cb-a0a6-304e-a946-84bae63edbff | -11.6277 | -43.717201 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ccef415-d720-35d8-902d-17271bfec1dd | -4.6694 | -48.9683 | 2026-10-09 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1d7ed17-6c43-3cc8-8bf1-2b0d191c1450 | -6.9401 | -43.666698 | 2026-10-09 00:28:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e05427c6-d53b-3e2b-9f16-d9764e805dbc | -11.8561 | -43.5891 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f6d56cb-b00f-34af-95e4-64128e5337dc | -11.6602 | -43.679798 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae84a36d-4567-31ba-b825-3b502b12ceed | -14.0865 | -43.778999 | 2026-10-09 00:28:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 963caf46-9854-3250-acc7-4347114fd0de | -5.3502 | -45.174702 | 2026-10-09 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98207995-5dac-392d-960d-3e21da82c35d | -5.3244 | -43.421501 | 2026-10-09 00:28:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aeada342-c85e-37bf-aea4-8b3d1547e660 | -11.2158 | -45.2589 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cdccafda-059b-3d33-bb39-82a6c8d472c1 | -7.4002 | -44.759602 | 2026-10-09 00:28:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 75d1d7fa-2197-3374-a4e2-b8245bc280e3 | -6.1776 | -44.648102 | 2026-10-09 00:28:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5fd9d74b-a385-30c8-a5a8-81163be09f00 | -16.910101 | -40.896801 | 2026-10-09 00:28:00 | METOP-C | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a185a6c-b513-3fea-ab21-5f7a6feb5de4 | -8.9602 | -45.174801 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f51a5a0f-4461-39cf-90c7-aed2a8f6e0c4 | -6.8812 | -45.912998 | 2026-10-09 00:28:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 178e7fb7-1dcc-31c3-b69f-4c88cbdd62c0 | -6.1793 | -44.655102 | 2026-10-09 00:28:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e6a05c2-f010-3410-97d6-7f91bc4d9645 | -3.8431 | -44.148102 | 2026-10-09 00:28:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69c291a6-54c8-3f99-9298-b846b2cf946d | -7.1914 | -55.182999 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcd39fa9-eeb8-3607-8095-c34da23be51b | -3.2902 | -53.704399 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbf17664-6052-300f-9194-659817b80114 | -3.2894 | -54.0201 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5759cb2a-88ec-3f6b-a7f4-b7bf151281b7 | -4.6232 | -50.960701 | 2026-10-09 00:28:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9f36c89-c345-39c3-aa3c-ccfcd325f443 | -2.8649 | -54.1772 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af1fbcd2-70ae-396f-a193-2b267d607d6b | -4.6724 | -46.308899 | 2026-10-09 00:28:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1da4eefa-8765-357a-9c33-1e3d110eb2bb | -5.9968 | -40.944 | 2026-10-09 00:28:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2eef0a37-746d-3208-85da-00a8c5fa43cf | -6.9617 | -45.2742 | 2026-10-09 00:28:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 775428d9-06a4-367b-b212-691deff03d37 | -3.2962 | -49.131001 | 2026-10-09 00:28:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a6523b2-c58f-35d9-9160-2f182698ca96 | -13.753 | -43.627399 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 73336cea-66c5-3647-9d4c-f293bb6d82db | -13.2623 | -44.008801 | 2026-10-09 00:28:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8b5edfc-b6b9-3c4f-98b2-87486d48706e | -10.4137 | -47.294399 | 2026-10-09 00:28:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c7fc359-90c8-34a9-85e0-41edab2949b2 | -13.1822 | -54.346802 | 2026-10-09 00:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a411bba9-5979-3b29-b798-54a862d8e358 | -2.9617 | -54.107399 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f25a0d5-df2d-3e00-b797-1ea658102f96 | -7.2206 | -55.176998 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b30ce156-3081-33c8-bdc3-8736507a3a49 | -13.7156 | -49.138699 | 2026-10-09 00:28:00 | METOP-C | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3bb0dd7e-607c-343e-bbca-1cd8807313b8 | -2.7691 | -54.068802 | 2026-10-09 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec715bb6-1d13-3383-acdc-51559ecdb8ea | -5.8697 | -49.8764 | 2026-10-09 00:28:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ca96711-baa8-349d-8493-701207cb10fb | -1.5907 | -47.349998 | 2026-10-09 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76b9a36b-e349-385b-99db-9c22d004f293 | -13.5011 | -44.3811 | 2026-10-09 00:28:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7b1aada-11be-333c-bbd5-0a275bb7c5db | -7.1869 | -55.161598 | 2026-10-09 00:28:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc624779-17cb-30df-8029-8b00f558acf9 | -3.1154 | -54.155602 | 2026-10-09 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10726a9e-f318-38d5-a6db-fd8910996fc5 | -8.9096 | -45.1791 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0bd3bf2c-6a75-35d5-9a87-1adec1338f81 | -14.9941 | -44.055801 | 2026-10-09 00:28:00 | METOP-C | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| f972dbf9-5563-3a6e-8b00-8160acdec486 | -13.7514 | -43.6203 | 2026-10-09 00:28:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3f9f327b-5df3-31b2-b747-014e6df4e867 | -11.0936 | -43.997398 | 2026-10-09 00:28:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 235a20fe-946a-3251-a2f2-bde1d53b83c7 | -5.1712 | -45.607101 | 2026-10-09 00:28:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa5b8876-478d-3484-bc85-ef188e4e322e | -16.131399 | -43.751701 | 2026-10-09 00:28:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 30454724-b58f-327f-87c0-48d77e863614 | -11.6228 | -43.695999 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a9ebd71-3b3a-3dd1-a4af-6c3896eafd6e | -14.9312 | -48.102001 | 2026-10-09 00:28:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 54c3aac7-858e-363b-9699-5bbbad5437dd | -4.9391 | -45.673901 | 2026-10-09 00:28:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2406c20-8550-3638-a994-6fe39a030b0e | -9.1208 | -45.836201 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6e8b6dd6-c1d8-366c-96ca-e56b2820b340 | -11.2734 | -45.194401 | 2026-10-09 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4956647e-b2c7-35e6-b3e7-beae3b274216 | -6.044 | -44.0284 | 2026-10-09 00:28:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70fd9832-297a-3acf-b35d-a10fde6ff276 | -8.8936 | -44.928699 | 2026-10-09 00:28:00 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dfeebf9d-27e1-3f65-bf0d-211884d7b04e | -3.5338 | -54.7047 | 2026-10-09 00:28:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50c53e8d-d0b4-36a2-a24e-d9e69d868650 | -16.520201 | -42.507301 | 2026-10-09 00:28:00 | METOP-C | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2f631297-888f-33b0-9b64-4289874941ba | -5.4449 | -43.451302 | 2026-10-09 00:28:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be6f8c0d-2f37-326d-8444-a58bc6ad42df | -11.9947 | -43.474201 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 454107dd-d042-34c0-84a7-2a9eb481f3d6 | -12.0029 | -43.464802 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5667b173-6970-3215-a4b4-31350059f180 | -11.7452 | -43.645 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e9731a05-f803-30c4-8d67-fce9febd5483 | -3.0901 | -53.951099 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 748e62c7-6e73-3e04-9acf-adbbe4989ac3 | -1.1076 | -54.183102 | 2026-10-09 00:28:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d02b7a4f-008f-3511-9e3e-a8fe24408dd4 | -11.3226 | -46.661999 | 2026-10-09 00:28:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ec214d7-17ae-3895-8b8f-39047b32b45d | -15.1073 | -43.6427 | 2026-10-09 00:28:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| a34d133a-9d70-34f0-ba5d-5fae0bb45a9d | -11.6358 | -43.707901 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab27bdc4-9a12-3deb-bcb3-c9402ada3a8a | -6.0359 | -44.037998 | 2026-10-09 00:28:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea10a11c-0825-3c12-b22c-cc3a9fb192e8 | -12.0077 | -43.441101 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c024be08-70de-3727-8596-0f49d8904649 | -5.3448 | -45.7337 | 2026-10-09 00:28:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 75d0caca-63c9-3e2f-8eb8-404568f53098 | -5.9513 | -55.3507 | 2026-10-09 00:28:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b45e5c0a-7130-32bf-a23a-e393b1fdbf97 | -12.0404 | -43.448502 | 2026-10-09 00:28:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f50db286-f228-36ee-83ec-6a3458650e41 | -8.9618 | -45.181702 | 2026-10-09 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9e132f63-1396-30c5-9ca9-c0d5a1d8fd6a | -9.2709 | -45.634399 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fbed89fa-824e-3302-bbb1-14ded59304ef | -11.0886 | -44.065102 | 2026-10-09 00:28:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e265d4b6-2b8f-3631-9f7d-0f4e07a9ad40 | -11.582 | -43.653301 | 2026-10-09 00:28:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 528529cf-38ea-31d2-a784-c1ca7d6214bb | -9.2725 | -45.6413 | 2026-10-09 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 226e17a5-35b1-3bee-99d8-f8d193efcd0c | -2.7565 | -54.1036 | 2026-10-09 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b069c837-898c-347d-9998-bcb9d7bf2e04 | -3.0922 | -53.778301 | 2026-10-09 00:28:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f90d3a06-54fb-3964-96b5-0edb9592bac8 | -15.9649 | -40.8372 | 2026-10-09 00:28:00 | METOP-C | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6f7e1cdd-cde5-3c19-93db-f0dbe5744710 | -7.1059 | -42.526199 | 2026-10-09 00:28:00 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fb2a5c10-2372-3448-8e04-48c2f05f6382 | -3.347 | -50.399502 | 2026-10-09 00:28:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f9d2659-29dd-3689-92c8-548105d8ae0d | -8.7077 | -38.6903 | 2026-10-09 00:28:00 | METOP-C | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README33.md)
