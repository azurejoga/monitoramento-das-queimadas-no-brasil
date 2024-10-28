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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da8b8f93-25d7-3bef-8a90-264e831c819b | -3.84975 | -45.72686 | 2024-10-28 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2c4c417-a2c0-30da-bd71-2a8e9a5ca218 | -5.24438 | -45.40637 | 2024-10-28 03:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0ae4630-f864-37f7-9e6d-63c19e2999ae | -5.24367 | -45.41042 | 2024-10-28 03:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17a6e431-7910-3b46-87ab-2d47eacb63c3 | -5.23921 | -45.40136 | 2024-10-28 03:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92d05ce9-5928-368e-9eac-edf6f754320f | -5.23849 | -45.40543 | 2024-10-28 03:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1872d558-23c2-39af-b6da-976e65d6b5b9 | -5.23779 | -45.4094 | 2024-10-28 03:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fd0eb0c-1ace-38af-9adb-4a8297d12dcb | -5.18544 | -46.19973 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bda6e23e-5af0-3f52-9fa0-8a051e7750e5 | -5.11519 | -46.03194 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 624a8efb-78d8-3ed4-9ac2-2e69eb9e5cd0 | -3.45629 | -46.33006 | 2024-10-28 03:40:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b88fdc11-5e2a-3432-997a-569f05867b11 | -3.45571 | -46.32967 | 2024-10-28 03:40:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ac2b4a12-44cf-3fad-85a6-6cfd0becde03 | -3.45539 | -46.33521 | 2024-10-28 03:40:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c3869113-5928-37a3-aa01-e4847b92102f | -3.45485 | -46.33483 | 2024-10-28 03:40:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2db20c45-3a59-3c0e-97dc-6ffb934048b3 | -3.40546 | -46.31526 | 2024-10-28 03:40:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6e5081b0-edf2-365e-821e-0d64c999335c | -3.40457 | -46.32052 | 2024-10-28 03:40:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5931ccc8-c0e5-3096-a954-66dba8d8e95d | -3.40368 | -46.32573 | 2024-10-28 03:40:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 12da1307-9efa-3632-b0ed-e253ab29893c | -3.39817 | -46.31937 | 2024-10-28 03:40:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f16257c7-6eff-340b-a93e-e2c424989e34 | -3.26999 | -46.21482 | 2024-10-28 03:40:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 465f693f-6c3a-3fa3-82e1-c787a65e943c | -3.2636 | -46.21381 | 2024-10-28 03:40:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 410a15b7-3a5a-35cd-a427-c68b6f05c270 | -3.17063 | -46.6053 | 2024-10-28 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d60b9e30-5a48-33b8-a34d-7820e3276a22 | -3.1697 | -46.61084 | 2024-10-28 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0270187a-a718-3c6f-8ffe-683af12f923f | -3.1685 | -46.60785 | 2024-10-28 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3761606e-0b52-3e9f-a1ed-3e782dee7aa9 | -3.16753 | -46.61337 | 2024-10-28 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e97b41f6-3ca9-31ba-bb1e-79fcd72afd8c | -3.16316 | -46.60972 | 2024-10-28 03:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b2a62b1-f562-3e57-a5fb-762962fdd0ea | -2.54871 | -47.32259 | 2024-10-28 03:40:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79048c7f-7214-3a60-9201-eca0c64f83a8 | -2.54869 | -47.32225 | 2024-10-28 03:40:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 986989d3-4211-3c98-82d0-baccd8e9482a | -2.54295 | -47.31493 | 2024-10-28 03:40:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f263e103-bb32-3de5-baf1-57b1098b8b7d | -2.54289 | -47.31452 | 2024-10-28 03:40:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43ce7149-2207-39a3-9b42-397854d14088 | -3.24383 | -46.0138 | 2024-10-28 03:40:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 339045dc-17f9-32f0-9bb2-bee05916cb27 | -3.23753 | -46.01275 | 2024-10-28 03:40:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c103e1d0-744b-34c3-8abe-42de21110077 | -3.23501 | -46.02763 | 2024-10-28 03:40:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c2da1d6-4e82-3794-a378-c14783737dec | -2.54474 | -45.98633 | 2024-10-28 03:40:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d08d7146-f408-349e-bab4-10b53a98dbab | -2.54387 | -45.99141 | 2024-10-28 03:40:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9e09d54-1cdd-39bc-b67e-243999da4076 | -2.54215 | -45.98927 | 2024-10-28 03:40:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 99ead2fe-7452-3649-8bce-99d7e6d4af3f | -2.50608 | -46.08894 | 2024-10-28 03:40:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4376a6a8-62cd-3fc2-9365-79647f3511e2 | -4.77472 | -46.39922 | 2024-10-28 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 9dd81286-5e59-3111-aeeb-f2478224d333 | -4.76929 | -46.39313 | 2024-10-28 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| ebe57a34-6f23-3d43-9930-685af20f7e14 | -4.76837 | -46.39841 | 2024-10-28 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| e8c51130-4504-37f7-983c-31357f68198f | -4.76741 | -46.40388 | 2024-10-28 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 60a69b59-ddcb-3b9b-84d0-3bada7d626db | -4.76292 | -46.39245 | 2024-10-28 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67c9f73e-8379-3e31-9206-2fad4672e4b1 | -4.76202 | -46.39761 | 2024-10-28 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fef5f945-face-3b3f-8c0d-1e88e187c62c | -4.76109 | -46.4029 | 2024-10-28 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 951dc85a-3b26-33dc-8759-c49ef3855696 | -4.74457 | -46.80125 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1bb418d0-42cc-35a1-af90-98bcb6610d5e | -4.74456 | -46.79988 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35858297-cd1d-3daa-9b3f-ac50d68bacdd | -4.74365 | -46.80518 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddb7f017-1e0c-370d-a895-37166bf704f6 | -4.73811 | -46.79871 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 020c8f5f-acf7-359d-bd41-3acfca09d9fb | -1.09517 | -47.24205 | 2024-10-28 03:40:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a074263-c08f-3574-b9d5-f4c2334254a9 | -4.7381 | -46.8002 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b180ebb8-2291-356f-99eb-5f5c3f7ab828 | -4.73713 | -46.80437 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c75fdaa8-5c53-3329-8c52-d2bbd192f3ab | -4.73711 | -46.80567 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 45c3ffce-ba8f-3ab4-9fdf-e5886314a675 | -4.68241 | -46.66281 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa5e1c07-492f-363b-ae38-47dad0063017 | -4.67691 | -46.65385 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e5c3abe-70a6-33b8-b741-4f2e8515c465 | -4.67689 | -46.65668 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1955e664-93af-39a7-a067-c90a7005a178 | -4.67604 | -46.65891 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fdea852c-b04f-375a-b058-5b7792f810d0 | -4.67599 | -46.66173 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e88179dc-7634-3a4f-9ac5-ec3512549934 | -4.67514 | -46.66418 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 82089333-a5b8-3363-a6e5-41416ad3a2c6 | -4.67046 | -46.65571 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa084ada-fa53-38fd-8bd1-38649dfe13ee | -4.54632 | -46.60832 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c793335b-df4c-3e27-9bde-51df990f2ca7 | -4.54539 | -46.60652 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6652d945-de68-3870-a50d-fecb589dbc1c | -4.54443 | -46.61205 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e23e3f93-721b-36e2-8434-35d43fae813e | -4.53984 | -46.60763 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a639ee0-ab77-33d4-930f-3d07b0cfc93b | -4.53885 | -46.61314 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a9d805f3-437d-3956-864a-b6e05a9b8943 | -4.53795 | -46.6114 | 2024-10-28 03:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4a4fda9-6d44-3c30-ba92-793cb1208f07 | -4.51768 | -46.46424 | 2024-10-28 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8762ded6-18ad-3540-9bd2-6e1c7c79f3d9 | -4.23863 | -46.87762 | 2024-10-28 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 27d9d93e-3fbd-3b20-8ab8-ce0c95719647 | -4.23761 | -46.88342 | 2024-10-28 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f3cefc20-360f-3a53-9357-4c1c6f363a42 | -4.18579 | -46.38662 | 2024-10-28 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55c90bab-611c-3de1-a2d2-bf2463324ef2 | -4.18354 | -46.38712 | 2024-10-28 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 660b749c-e98f-3e21-a035-4f1f5fb190b5 | -4.17953 | -46.38503 | 2024-10-28 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 740da299-8fee-3110-831b-a949a67ad648 | -4.1786 | -46.39028 | 2024-10-28 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 99986fdf-7702-3db2-ac13-31dae6d2e9a6 | -4.17725 | -46.38568 | 2024-10-28 03:40:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 651ba8bb-964b-34a4-b63f-5e10f7bf09db | -4.13006 | -47.32683 | 2024-10-28 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8b9cf846-f0a1-3ce0-938c-879e401545bc | -4.12901 | -47.33301 | 2024-10-28 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ef2064bd-9bff-3f5a-90f7-78532f73b4c0 | -4.12524 | -47.3254 | 2024-10-28 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 62f4146c-76dd-34d4-bce5-e750024c0595 | -4.12414 | -47.3316 | 2024-10-28 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b282f0dc-837a-3368-a2c7-5f16688db3b7 | -4.12335 | -47.32559 | 2024-10-28 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 23306a49-5bb4-31a3-aec0-733bb0a00ae7 | -4.12228 | -47.33183 | 2024-10-28 03:40:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ba7d3102-3319-3de7-a09c-0cdcb839e6ec | -3.98902 | -46.48085 | 2024-10-28 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1f4154d9-925b-3914-b657-f4241551685f | -3.98811 | -46.48606 | 2024-10-28 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 05ee329f-00b3-33d6-83e2-671a98b64a7b | -3.96805 | -46.21127 | 2024-10-28 03:40:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ac8f6ab-7af6-3695-8e7a-a633d1a73165 | -3.96175 | -46.21012 | 2024-10-28 03:40:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78cde2da-2e51-360a-a38b-c76f4c66b04e | -3.96086 | -46.21534 | 2024-10-28 03:40:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b369b3a8-c012-375c-b5bf-80224f9f062a | -3.95563 | -46.40836 | 2024-10-28 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d08eebf5-112d-3296-bdad-de7e6e3c55a5 | -3.95438 | -46.40653 | 2024-10-28 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6ddac8af-b2de-3579-bb3a-6822b9c2bac1 | -3.95389 | -46.41816 | 2024-10-28 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8c1fea08-d6a1-3a5f-bac4-ee7e0c4c1097 | -3.95363 | -46.4109 | 2024-10-28 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6946fc3b-810b-3f8c-8e22-8c4658815dad | -3.90824 | -46.44546 | 2024-10-28 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a80c3d26-824d-32f5-889b-449ddec737eb | -3.90733 | -46.45072 | 2024-10-28 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d9c599f-ee49-36ad-9699-0dac1c8a3373 | -3.61723 | -47.2638 | 2024-10-28 03:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 992eb347-8dae-3acb-99fb-2311fed30de3 | -3.61302 | -47.26021 | 2024-10-28 03:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8b54586d-4616-3140-9116-9d609efd7281 | -3.61058 | -47.26202 | 2024-10-28 03:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 860a09a6-6fb8-3146-848d-d2881181c096 | -3.59534 | -47.28158 | 2024-10-28 03:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f6d8b77-f38b-3ccb-8f2d-4cfc7ee253c2 | -3.59305 | -47.28341 | 2024-10-28 03:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b3a2cf0-8786-3b98-ac1a-d999116bcb98 | -3.58871 | -47.27968 | 2024-10-28 03:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7859be11-a442-348c-a5af-19ea07c71aca | -3.58639 | -47.28163 | 2024-10-28 03:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aedeeb9-4ac4-323b-a149-36ef6bec8eb3 | -1.78113 | -47.84315 | 2024-10-28 03:40:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04e25ea5-7279-3fb8-a6e6-74d9586537a8 | -1.08928 | -47.23422 | 2024-10-28 03:40:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f127b08-1581-3f3f-b018-585073894a52 | -1.08819 | -47.24084 | 2024-10-28 03:40:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f509fa8e-7737-33f2-9e5d-6cd7290a619a | -2.52784 | -47.44425 | 2024-10-28 03:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4503ce0-8379-3e46-be48-bbe9f64f42c7 | -2.52171 | -47.44278 | 2024-10-28 03:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b5060250-7627-3a32-a0f6-4154d357a34a | -2.52096 | -47.4428 | 2024-10-28 03:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |


[Clique aqui para ver as próximas entradas](README26.md)
