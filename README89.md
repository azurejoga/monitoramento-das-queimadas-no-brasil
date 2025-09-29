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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68f16390-4c9e-3c16-8546-0d0fefbe1ca5 | -10.6239 | -48.5386 | 2025-09-29 12:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| ffc6cc8d-acfd-303a-a46b-e3878d2f0c8f | -12.9435 | -46.7655 | 2025-09-29 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 99d09d4e-e9aa-3add-929e-6dd55ae5c7d8 | -13.235 | -50.9476 | 2025-09-29 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| cba9315f-ae6b-3be2-b7a7-79d294548901 | -11.4405 | -45.0461 | 2025-09-29 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 6731bb94-1b65-3424-9865-4680947fd9c8 | -11.4409 | -45.0229 | 2025-09-29 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| d4485bd2-d824-3861-bb19-100e5b0a3b74 | -14.6049 | -45.0161 | 2025-09-29 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| e28bd2fd-b4cb-3551-90df-2e7a6217d8a2 | -11.3443 | -45.0828 | 2025-09-29 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 969def6b-84ee-33d2-9bcd-c36aaa044996 | -14.5331 | -48.4491 | 2025-09-29 12:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 394e2257-e7a6-38d1-8459-f85d0e860e0b | -7.8566 | -46.7527 | 2025-09-29 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 6873cad7-13a3-351a-af56-2e1a8f37fbb0 | -8.2854 | -45.4772 | 2025-09-29 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| a6f9fcdb-2af8-335a-9a1b-7cb300cf07c7 | -7.2402 | -44.7812 | 2025-09-29 12:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e751e7e0-2906-3a78-8332-3ab53e150a1d | -8.2662 | -45.5018 | 2025-09-29 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| edeca801-3ce6-3f8f-b7c1-cf568437a39f | -8.2659 | -45.5244 | 2025-09-29 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 9328ac26-eed9-35e4-8ce9-e8f7d22875d3 | -11.4405 | -45.0461 | 2025-09-29 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 1cf93da3-7d80-30bd-8fdf-2d9e80ef3ab4 | -7.8165 | -46.9781 | 2025-09-29 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| fba98891-b823-371c-85d0-81052229da42 | -13.2005 | -50.716 | 2025-09-29 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 87734ea1-62e1-3b66-9620-1cc976b51e84 | -15.0496 | -46.9675 | 2025-09-29 12:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 92.4 |
| c4fcf48d-313f-31d4-89f3-d724b45a4518 | -7.4488 | -46.299 | 2025-09-29 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| d9719fd2-143c-39a1-8c3b-8ba7dc95ad88 | -7.3653 | -42.1058 | 2025-09-29 12:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 296b4363-b5fc-329a-95a4-13eace5f063d | -13.1816 | -50.6969 | 2025-09-29 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 2002662d-87f1-326c-bf26-2bf8833c3e3b | -7.8378 | -46.7544 | 2025-09-29 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 0d864cea-89dd-343b-aefe-4cf01584c930 | -9.8852 | -45.9122 | 2025-09-29 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 663647ef-7300-39d2-9506-60ce9dbf4d33 | -14.698 | -45.2093 | 2025-09-29 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 5ad57f87-6969-36c8-9bad-f7d67fa3bd01 | -11.3095 | -43.7844 | 2025-09-29 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| c558103f-538c-350e-8aad-67ff7fa9bcc9 | -7.2214 | -44.783 | 2025-09-29 12:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a3779efa-881d-30e9-b9fe-83ba7533da5b | -14.7176 | -45.2057 | 2025-09-29 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 719d3081-d9a9-3e3f-82bf-690dedc6f92e | -7.8163 | -47.0003 | 2025-09-29 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 4883ea87-fec8-3890-86a8-7193020c4ef1 | -9.8848 | -45.9349 | 2025-09-29 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| a018f6c6-77a6-34df-b7a1-e2a8a5fc05da | -7.4676 | -46.2974 | 2025-09-29 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 5b8297c2-9784-3208-ae85-c4119b1766c1 | -10.8055 | -45.3637 | 2025-09-29 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| f66cf048-a87e-3520-9125-7b88e379c79a | -12.863 | -46.9582 | 2025-09-29 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 6cbdd6d7-cb97-3c18-a557-c98ffd3ab9c9 | -11.3638 | -45.057 | 2025-09-29 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 620027cd-1926-366c-9b33-f7b7692214df | -11.3826 | -45.0774 | 2025-09-29 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 0a889207-10ac-3cf9-9f89-a46dae85d951 | -9.3708 | -47.556 | 2025-09-29 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 84a704ae-0f23-3a32-b953-259716064f7f | -11.4409 | -45.0229 | 2025-09-29 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| af6eaf63-dc0a-369e-9a58-d37e2f9d04b2 | -15.219 | -50.1071 | 2025-09-29 12:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e2415297-0be2-35e2-a56a-70b6ad0ef2e5 | -13.2346 | -50.9691 | 2025-09-29 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 370.3 |
| 72972ced-14cf-3734-9bfc-c3dfb2153d72 | -7.9006 | -44.6035 | 2025-09-29 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| fcb9d5cc-6fc6-36a8-b8f7-63173099c445 | -13.235 | -50.9476 | 2025-09-29 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 10181ea1-9d64-3de0-8fcb-97d9854ec722 | -6.4319 | -43.0707 | 2025-09-29 12:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 61b14b16-07f0-3d73-8f0b-4c2645654642 | -10.6239 | -48.5386 | 2025-09-29 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 0e6e2d5e-17c9-39ea-a976-744f0e8c84a5 | -13.1816 | -50.6969 | 2025-09-29 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 4e2bb288-acfc-3ce2-8103-81210ee60634 | -14.6049 | -45.0161 | 2025-09-29 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 233.8 |
| e5c493e8-a7f1-34ee-b2f6-2c437794fbf5 | -7.2216 | -44.7601 | 2025-09-29 12:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 6947c75b-6214-30ca-ace8-f641699d7ce0 | -7.8163 | -47.0003 | 2025-09-29 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| d64906d4-0b4d-3aec-a2cc-f03755e49af2 | -12.863 | -46.9582 | 2025-09-29 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 53e67a82-4aa4-38fc-8399-68797fb9c4b1 | -7.7414 | -46.9848 | 2025-09-29 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| f5cc9262-f18d-310f-b413-5f017026f14f | -6.4317 | -43.0942 | 2025-09-29 12:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| fbb5aa5f-de0c-3fe9-b059-d5fce476d7e7 | -7.5447 | -46.1115 | 2025-09-29 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 1a11f9c6-d1a9-3e34-aff8-a09670f7fea8 | -10.6242 | -48.5167 | 2025-09-29 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 94a57dda-a00d-3081-bfb5-8bd61bc2a913 | -9.8852 | -45.9122 | 2025-09-29 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 05b419a5-141f-3c62-b8e7-b766d10861a0 | -7.7226 | -46.9865 | 2025-09-29 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| db0f1e2a-be65-3899-bbc7-84a788210454 | -8.2854 | -45.4772 | 2025-09-29 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 9e69f7e7-151e-3425-aabb-f66bdbfccc98 | -13.235 | -50.9476 | 2025-09-29 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 82433463-ed19-3cde-857b-ca08ff1a5bce | -7.8165 | -46.9781 | 2025-09-29 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| c508d068-cbc9-39c9-80e0-da2d495b510d | -11.4405 | -45.0461 | 2025-09-29 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 4270e909-a773-324f-81e7-b8db8ef94ec1 | -6.7482 | -43.3704 | 2025-09-29 12:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 02800542-5a82-3cc4-94de-35101bee2d7a | -11.9247 | -48.0495 | 2025-09-29 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 08c4a2c1-3910-3b76-8e62-63d241da6448 | -15.6127 | -46.2465 | 2025-09-29 12:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 7314aa2b-990a-3ea0-844d-e9f9a6d77188 | -9.9872 | -45.4228 | 2025-09-29 12:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 38abeec5-eeed-3653-b2c0-8516ae62eb5a | -14.698 | -45.2093 | 2025-09-29 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 04967b7c-b854-3a43-91b0-ea07cf141694 | -7.3464 | -42.1078 | 2025-09-29 12:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 49ca9fe8-952d-3b5c-a727-92ce2156c340 | -9.7671 | -46.2196 | 2025-09-29 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 51571c06-7527-371c-a74f-2ea812d13fe9 | -13.2346 | -50.9691 | 2025-09-29 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 441.3 |
| cb404b64-6cdc-3ce6-9bbf-80dc76d79dd3 | -14.7176 | -45.2057 | 2025-09-29 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| b5234eec-546b-3629-ae16-96e09ae7676f | -7.2402 | -44.7812 | 2025-09-29 12:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 9e9a92c3-753f-349b-9f31-075f432550f1 | -10.0062 | -45.4204 | 2025-09-29 12:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| cfa43630-3bda-3057-b182-58046195f0cb | -8.0034 | -47.0497 | 2025-09-29 12:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 13e67594-45e8-3944-bb5e-dc91ad4aef38 | -8.1614 | -46.3899 | 2025-09-29 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| cf9bef2f-ac5f-31a6-a21a-a6a1ae74f581 | -11.8482 | -51.7916 | 2025-09-29 12:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 0ea3b760-cd0b-3721-be66-f5e1f7838486 | -15.8682 | -46.2214 | 2025-09-29 12:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 106.9 |
| c8b5a2f7-83cf-387b-9d22-87ca846dbc5e | -9.7674 | -46.1971 | 2025-09-29 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| a3f66bea-abf4-3be4-90ca-14ee8bc7f279 | -6.9692 | -43.7927 | 2025-09-29 12:50:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 1772760d-c917-311a-8397-275d38614ea0 | -7.3653 | -42.1058 | 2025-09-29 12:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 108.6 |
| 34b98c1d-e02c-3fbd-ab34-7154e1e4044b | -7.4676 | -46.2974 | 2025-09-29 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 149.2 |
| c215138b-9bd4-3f06-a499-6887aa5158ce | -7.2214 | -44.783 | 2025-09-29 12:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 100790de-0cb7-3c28-8b2b-7ff17e80e7d7 | -15.219 | -50.1071 | 2025-09-29 12:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 554e052e-f5f1-35ff-8a56-75900ec09c2e | -7.8378 | -46.7544 | 2025-09-29 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b68b739a-b28f-370d-be6d-0bfabc952a4c | -9.8848 | -45.9349 | 2025-09-29 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0df3a80a-416f-3553-bc5e-9c86a544ca89 | -11.4409 | -45.0229 | 2025-09-29 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 3f273a5b-a224-3c42-9590-29bdfeb5b849 | -8.2662 | -45.5018 | 2025-09-29 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| af3ece04-498b-3dc7-9fd3-22ff866a8c42 | -8.2659 | -45.5244 | 2025-09-29 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 7080aa42-23fa-3ffa-b0a6-cfb217ac96a7 | -11.3638 | -45.057 | 2025-09-29 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 24ddeb07-ba00-3a99-aea2-ad07946c34ec | -14.5331 | -48.4491 | 2025-09-29 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| e9200b3d-038f-35ff-89a2-e2f1bcf66e56 | -15.5169 | -47.9284 | 2025-09-29 12:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 94d3cc48-0e8e-3f72-9339-c4a9b711f42e | -13.3796 | -48.1577 | 2025-09-29 12:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 7d4bfe1c-04a9-36bf-8571-a19a5292bbbc | -11.3826 | -45.0774 | 2025-09-29 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| a0b00697-e1f0-3639-b75f-bbdaeb9ed13b | -9.1102 | -45.8653 | 2025-09-29 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| d3e72a06-9b40-319c-b667-801d93542fd9 | -13.011 | -49.4423 | 2025-09-29 12:50:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 071c0f4f-9fdf-3642-b2a9-7bff238bf805 | -7.8566 | -46.7527 | 2025-09-29 12:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 8e138b8a-be85-358e-b3dd-d7185f1b8ce1 | -11.925 | -48.0273 | 2025-09-29 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 3ad185b8-4e00-3454-a01e-d019bef96035 | -6.748 | -43.3938 | 2025-09-29 13:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 7363570d-c94b-3aea-934d-34ad2d7b92a0 | -11.925 | -48.0273 | 2025-09-29 13:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| fe9bc460-efb5-3320-9212-5c4f80f26da3 | -11.4409 | -45.0229 | 2025-09-29 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 057b2fb3-2229-3fd5-af86-59644edddb4b | -10.4022 | -48.1476 | 2025-09-29 13:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 3c728ba7-0203-3df4-84e5-73ece43afd3b | -12.9736 | -45.1819 | 2025-09-29 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| f983e12d-bc1e-31a0-8d31-5c981cfa7925 | -8.2848 | -45.5225 | 2025-09-29 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 257.6 |
| 15955ad7-77fb-3337-8ae9-800988dd3f5a | -14.698 | -45.2093 | 2025-09-29 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| c2c67c7a-3432-3fc6-b4e3-835a300045bc | -13.1816 | -50.6969 | 2025-09-29 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 60ec6293-952c-3e43-82e5-a1a50e6e81df | -11.4405 | -45.0461 | 2025-09-29 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |


[Clique aqui para ver as próximas entradas](README90.md)
