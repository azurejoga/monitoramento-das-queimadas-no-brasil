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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84914e9c-2151-31e5-b535-b7ced86e1158 | -4.81571 | -40.31799 | 2024-11-18 03:23:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 378237f0-392e-3de3-b5e6-b03fda7268f9 | -4.9051 | -44.0261 | 2024-11-18 03:23:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| c31d323e-1aef-3b01-86f1-0f4e6e633e97 | -6.74181 | -35.43103 | 2024-11-18 03:23:00 | NOAA-21 | SERTÃOZINHO | PARAÍBA | Brasil | 2515930 | 25 | 33 | nan | nan | nan | Caatinga | 7.4 |
| ac6e5b2d-c55c-3a15-be54-f2dd92cf8f9c | -5.61385 | -36.87078 | 2024-11-18 03:23:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3b04139c-2fd6-3f67-8516-7a63abcc1934 | -4.81807 | -40.31898 | 2024-11-18 03:23:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f8dbb55b-a2fe-3be9-98cc-69c28d8ce52b | -6.73866 | -35.4284 | 2024-11-18 03:23:00 | NOAA-21 | SERTÃOZINHO | PARAÍBA | Brasil | 2515930 | 25 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a8a91b09-4f71-3549-b156-759996cbaa57 | -4.81873 | -40.31505 | 2024-11-18 03:23:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ef11fd92-3929-314c-8bd2-143202dc9400 | -4.90235 | -44.02601 | 2024-11-18 03:23:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 26697a2d-53b6-3bfe-b214-09ebe1cda8b8 | -6.66698 | -34.98114 | 2024-11-18 03:23:00 | NOAA-21 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| a1534f79-b8a6-3405-8c58-922f2ff3cbea | -7.40007 | -42.76812 | 2024-11-18 03:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| ade61443-08ee-3771-846f-5c31ce02675c | -7.85701 | -35.437 | 2024-11-18 03:25:00 | NOAA-21 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8deb6cfb-6cf7-3ef3-b0e4-0fa03d67c73e | -11.11701 | -45.29359 | 2024-11-18 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dde3a49-8fe4-3061-bbe2-1baa2bd45ab0 | -7.6654 | -39.29302 | 2024-11-18 03:25:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0a87786e-9cbe-3aed-9995-bf8ee15d1d3a | -10.23903 | -36.50895 | 2024-11-18 03:25:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ea545d76-7835-3be7-a954-317235fe7c2f | -7.00198 | -37.8982 | 2024-11-18 03:25:00 | NOAA-21 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 8.4 |
| bddc263e-4457-3d22-9e79-72f82ef1185a | -9.19981 | -35.72139 | 2024-11-18 03:25:00 | NOAA-21 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1304d232-39c6-339a-b175-44c72c2aec0d | -12.15859 | -40.94633 | 2024-11-18 03:25:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4927eb97-917b-3349-8ce8-978bb3d85a27 | -11.12392 | -45.29477 | 2024-11-18 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90cc5cba-44e3-31c7-a5af-d5be75ab1317 | -7.39732 | -42.76582 | 2024-11-18 03:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| cb4455f8-c798-327a-8cea-76ee5e8a9520 | -10.87547 | -43.367 | 2024-11-18 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c9eca25c-d788-3f5e-a342-9953ed39cb98 | -7.53506 | -35.31514 | 2024-11-18 03:25:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 22dc0287-982d-39b3-b104-b860a7609f09 | -10.52169 | -36.74228 | 2024-11-18 03:25:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 12a9b827-058f-3d70-8487-5c4354d81e0d | -7.39822 | -42.76091 | 2024-11-18 03:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 46eaa4d3-fad6-3a8b-a5ac-ec0ecbd85466 | -11.48574 | -42.94892 | 2024-11-18 03:25:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7d934f06-ba3e-3f7f-86f2-842f9b4fd853 | -10.50156 | -36.73841 | 2024-11-18 03:25:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8983390b-9d48-3c96-978e-d39278f766af | -7.40099 | -42.76324 | 2024-11-18 03:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 02a99283-b302-3f82-be19-2cc2ec2a3348 | -7.74369 | -37.78654 | 2024-11-18 03:25:00 | NOAA-21 | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a22a4093-4454-3dac-ae71-9662d94a422b | -7.5473 | -35.21895 | 2024-11-18 03:25:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 509d0fa1-eeea-3be6-a052-74d1bcd798b5 | -7.74235 | -37.78709 | 2024-11-18 03:25:00 | NOAA-21 | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f01b9ce6-dad1-3dc1-a237-e3a41e7a4548 | -10.52572 | -36.74303 | 2024-11-18 03:25:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 17838764-80f8-31d6-89f0-db3eba0b1327 | -7.53894 | -35.31572 | 2024-11-18 03:25:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c3107315-15c9-36d7-9ad8-8eae39c1270c | -10.23504 | -36.50824 | 2024-11-18 03:25:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 344692fd-2381-3e92-ba59-daf776e098af | -10.6953 | -37.04945 | 2024-11-18 03:25:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f4e1c2ca-6d0e-3cfc-90b7-f6836365ec4b | -22.90006 | -43.75023 | 2024-11-18 03:29:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bc3b3737-30f5-381d-9bce-55662f6be2fa | -1.2964 | -51.7204 | 2024-11-18 03:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| bfc229c3-8cc1-368b-b781-17fa3e75dff2 | -3.0542 | -54.4081 | 2024-11-18 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 275fbeb9-eb03-3cf5-b648-e777cf1f391f | -1.2964 | -51.741 | 2024-11-18 03:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 176.3 |
| 30faa235-6b7c-3d3d-8658-4c7562addc23 | -17.6063 | -57.5715 | 2024-11-18 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| de8aba0d-68f8-3bb7-b3b6-37420f8f233a | -2.5847 | -51.7181 | 2024-11-18 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 3d8935a3-a704-34e6-92b8-80dab2c7798f | -17.6059 | -57.5921 | 2024-11-18 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 35a55176-60e0-3d47-97ac-0d48197a65e9 | -1.3148 | -51.7408 | 2024-11-18 03:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 21c55b01-1790-31be-a4e5-3b292b4955cd | -1.7147 | -45.8307 | 2024-11-18 03:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 4e7284b9-d54a-3100-b483-be1f43c0e5f7 | -17.6256 | -57.5897 | 2024-11-18 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 2f3b7e16-ba07-3516-be5b-4b513602fae6 | -1.2964 | -51.7616 | 2024-11-18 03:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 2676e846-e77d-3dac-9dc0-d5430687565e | -17.626 | -57.5692 | 2024-11-18 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.9 |
| 0ab53c0f-12cb-3934-a7fa-8f7fe395c329 | -3.3452 | -50.4917 | 2024-11-18 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 7b891df9-db1c-3d35-b990-67775b7ec1ac | -27.66463 | -50.82587 | 2024-11-18 03:32:00 | NOAA-21 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 830b8c91-020c-3a05-ba05-be9513c3e664 | -27.66278 | -50.83267 | 2024-11-18 03:32:00 | NOAA-21 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 23bb31d0-a4cd-3cde-99f5-07dc1ab0389b | -17.626 | -57.5692 | 2024-11-18 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.6 |
| 4773a6e9-9736-368e-86c0-64ca8e9da0a4 | -1.2964 | -51.7204 | 2024-11-18 03:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| d7c5867c-1ef8-39b6-b55f-19b1327505ad | -1.2964 | -51.741 | 2024-11-18 03:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 491dd350-d2c6-3fbc-a239-d4bca8f51569 | -17.6063 | -57.5715 | 2024-11-18 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.9 |
| fa129e77-9155-3c6b-8de7-225b97722b01 | -1.3148 | -51.7408 | 2024-11-18 03:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 24007f3e-904a-3930-acd6-9903d8f1a0db | -3.0542 | -54.4081 | 2024-11-18 03:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 42687424-92e4-3186-ba5f-ae104a2b0310 | -17.6056 | -57.6126 | 2024-11-18 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| 7f621196-6f73-3e54-92cb-ed272be856b5 | -1.3148 | -51.7202 | 2024-11-18 03:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 991771fd-c28c-305f-b295-89b3dd89b851 | -17.6256 | -57.5897 | 2024-11-18 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| be1711eb-822c-3a72-8d30-3280ced898d5 | -1.7147 | -45.8307 | 2024-11-18 03:40:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| d85ffe2f-5957-3ddd-a150-15a166069886 | -14.286 | -57.624 | 2024-11-18 03:40:00 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 222e58ce-dfe8-319f-a29c-1b06e3c81912 | -2.5847 | -51.7181 | 2024-11-18 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| a978d23d-ab91-375e-aef9-9d736a1294d0 | -17.6059 | -57.5921 | 2024-11-18 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| a9c4518a-22f9-38f5-a100-25a768dc8666 | -1.2964 | -51.7616 | 2024-11-18 03:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| d8977600-1d44-35ba-ae79-0d95ccf664d8 | -3.18548 | -45.44207 | 2024-11-18 03:46:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d25a9e31-3f90-395d-82d5-1df8a02cc06e | -3.8912 | -46.62408 | 2024-11-18 03:46:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54671129-5699-398c-be0b-f0dd0554a66b | -6.4282 | -35.25233 | 2024-11-18 03:46:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 56627548-f528-3823-878d-eec4fdcd4d3f | -3.76364 | -45.95091 | 2024-11-18 03:46:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f28ded1-5b49-3567-bde4-f2650dd75bd5 | -4.80901 | -42.21011 | 2024-11-18 03:46:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b6f5c624-69f4-3639-8829-e1f32082e704 | -4.78998 | -40.40611 | 2024-11-18 03:46:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e6ecb371-b2d3-3ec1-a358-9a7f7b5d2f28 | -4.73131 | -44.43668 | 2024-11-18 03:46:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21c4c471-b65e-3bb6-a238-3bbb6aee86c5 | -1.75679 | -45.69012 | 2024-11-18 03:46:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03184382-083a-3b0e-8190-da4c034377c4 | -2.50522 | -47.24314 | 2024-11-18 03:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 14e5fef2-1a2c-3efd-a8a5-c38bd4e14359 | -6.50327 | -35.24126 | 2024-11-18 03:46:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f89977c4-841e-3967-970d-f8f7b10f3f17 | -4.81331 | -42.21081 | 2024-11-18 03:46:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2c1d64d4-392d-3802-ba42-05b4f2d33a83 | -10.44265 | -44.88361 | 2024-11-18 03:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 69866d29-aebd-3517-b7b3-e5d3bd2672fb | -3.16639 | -46.59357 | 2024-11-18 03:46:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a8fa108-dbd6-34c0-b0f0-efbb398cad94 | -9.30379 | -46.21335 | 2024-11-18 03:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5f244a8-cb0e-3b63-9791-4cb208d2e71c | -2.33849 | -49.13482 | 2024-11-18 03:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| de4314e9-7f47-35dd-9337-e59f84228aae | -1.70388 | -45.83022 | 2024-11-18 03:46:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1a1d5587-1d54-3fe3-baca-54c2e54f2ef0 | -7.71359 | -45.66229 | 2024-11-18 03:46:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fffb5b7-75e3-321e-8c80-e418595b2442 | -2.63016 | -46.83682 | 2024-11-18 03:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9b8ad63-911b-374e-b945-dc075b58dba4 | -1.76219 | -45.68851 | 2024-11-18 03:46:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1777e5c4-aecd-39f8-af82-305651aa58fe | -1.709 | -45.8353 | 2024-11-18 03:46:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 719c75df-4590-3e13-90be-b7e164bf9324 | -3.07621 | -48.07142 | 2024-11-18 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b37f8b20-3742-3496-9316-2c3ede16bab3 | -4.65678 | -44.08795 | 2024-11-18 03:46:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1e6051b-9683-3906-9774-a2883d4e07e5 | -2.46879 | -45.61818 | 2024-11-18 03:46:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d56969aa-407e-3500-a0a9-99926ae33ae4 | -3.13918 | -45.34853 | 2024-11-18 03:46:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15708486-d0f6-3a2f-bb65-3416f75c1bc2 | -11.14381 | -45.34494 | 2024-11-18 03:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 152fa8e3-fab8-3364-b91b-0278a749a5cc | -3.58018 | -45.20986 | 2024-11-18 03:46:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2427e6f-a372-3fd9-b7f9-00036cb14480 | -4.72627 | -44.43593 | 2024-11-18 03:46:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ece43ab2-ac91-30b5-83ff-22a5b4921144 | -4.74785 | -44.9113 | 2024-11-18 03:46:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5196dfb9-3447-308b-a146-e2ec58551d5f | -11.77069 | -40.90262 | 2024-11-18 03:46:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ce4c20a0-0515-3d5f-a930-1ba633845117 | -10.52145 | -36.74297 | 2024-11-18 03:46:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 92f85a88-35ba-37ca-b29d-76fb7053ae0b | -2.63023 | -46.83556 | 2024-11-18 03:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 522c08a3-8e04-35d1-8d40-bc2cba97b9b6 | -5.61246 | -36.87307 | 2024-11-18 03:46:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| abc6ccd7-1dae-3f32-814e-bc74793241d9 | -4.81624 | -40.31879 | 2024-11-18 03:46:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f9da089c-e4ee-3fac-a3bb-62d34effc8a2 | -3.76699 | -45.94837 | 2024-11-18 03:46:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81823169-b230-3358-aec3-9431f0ee9fb5 | -2.22718 | -46.46918 | 2024-11-18 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b15b01a1-8e1e-3db3-a9c2-74da138564f0 | -8.53601 | -39.5928 | 2024-11-18 03:46:00 | NPP-375D | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 08c5cb87-2f8a-30be-b5c8-09ad5e229759 | -3.19082 | -45.4454 | 2024-11-18 03:46:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd1144ee-0e13-3caf-acfe-d1ad4f1b12a8 | -10.522 | -36.73942 | 2024-11-18 03:46:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README15.md)
