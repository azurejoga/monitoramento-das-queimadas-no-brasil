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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 189cc530-455d-31d5-9941-424b1e424fdb | 1.18082 | -50.94448 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1114c1d6-5571-3443-bbb3-89965d468909 | 1.06396 | -51.00372 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b0eda48-34f0-3bb3-bed9-d6b05b23f33f | 1.24527 | -50.8827 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a336319-ec28-3642-97b4-621c119c1195 | 0.84401 | -51.8375 | 2026-09-16 04:55:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7535eecd-a96a-3cb6-a801-c7c930c2e5aa | -1.3318 | -47.78362 | 2026-09-16 04:55:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3bc0736-a09d-3456-9474-41eece33489e | 1.24303 | -50.89052 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fd30368-433d-3ec1-8c29-7fb38cc00734 | 1.24245 | -50.88688 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3ac9745-45a6-355e-9889-74c424264d43 | 1.20983 | -50.79069 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c684f042-e9fa-34bf-a6af-1bf526cb07a9 | -0.98191 | -47.50237 | 2026-09-16 04:55:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a053c132-f35e-3829-9986-2e0db661e6cf | 1.96163 | -50.95438 | 2026-09-16 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 962fb294-8915-395b-af6c-8279adf7ea32 | 1.21266 | -50.78652 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92e17e81-3644-3b74-a7bc-78826e241f22 | 2.58019 | -60.30429 | 2026-09-16 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 68fadd09-e686-3d58-a3df-5d8961a645e3 | -0.97713 | -47.50556 | 2026-09-16 04:55:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9e9b13d-b77c-3ca8-a0c4-8e4e4e3e3f32 | 1.9244 | -50.82698 | 2026-09-16 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83d80f0b-68ad-309b-81a7-b9df9f232994 | 4.75163 | -60.56949 | 2026-09-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b16e57b4-0fe3-34e8-aed4-dcaec10bd1bc | 1.18308 | -50.93666 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91354da6-26d9-3d85-84e3-0d63ad9eeac4 | 0.19847 | -51.35794 | 2026-09-16 04:55:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 088ee518-c8a3-38bd-a222-cf46ac0c9bf0 | 2.18946 | -50.90854 | 2026-09-16 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a42f7d9-31fa-33a1-aeb1-ad0e6e6945f9 | 4.74647 | -60.57039 | 2026-09-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13404f2c-cb37-3394-8c8e-7a89c84c1458 | 1.178 | -50.94864 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 537ec59e-154d-3151-b5df-eb0bc32355e0 | -0.92991 | -47.1926 | 2026-09-16 04:55:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9e1ad05-8fd4-379a-aba0-5442311faf78 | 1.21607 | -50.78597 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 067c18d0-9915-3404-a00a-8f000e1d4964 | 1.18647 | -50.93613 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 035134e6-c3eb-3843-835b-6593c10b1d96 | 2.70765 | -60.30127 | 2026-09-16 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9c2644e0-e6d8-32d8-abae-242a997d1141 | 1.2481 | -50.87852 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc5a887f-b5b1-359b-9868-579dc24f8ecd | 2.20902 | -50.89043 | 2026-09-16 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bea0eac-2f1d-305b-a0f2-62eb554758f5 | 2.20228 | -50.89148 | 2026-09-16 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15cee6f7-409d-3d69-b516-c43a9843e19d | 1.17349 | -50.96423 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f377dbe7-5142-3db8-b2bc-a1fc1b19f289 | 4.74789 | -60.56907 | 2026-09-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06e90566-bcaf-3ead-bcdd-0b9973454f30 | -1.21814 | -47.89108 | 2026-09-16 04:55:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef2ca40a-cd19-3837-bced-7232aa239f94 | 1.18422 | -50.94395 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 91e67782-83a7-31d8-9f89-52bd76348a49 | 1.18196 | -50.95174 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8082b110-27c4-30ea-819d-357f0f19a24f | 1.17292 | -50.9606 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2e9216da-0e90-39b9-a064-94b1f7660fa8 | 4.75304 | -60.56811 | 2026-09-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4240710b-3898-3bde-a817-1d9864cfa0db | 1.97176 | -50.93068 | 2026-09-16 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8ccc7a8-69e8-37fd-8c44-bb404c467d64 | 1.18365 | -50.9403 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4c96408b-f3ab-345b-8726-83cfb7c98da1 | -0.88518 | -47.56688 | 2026-09-16 04:55:00 | NOAA-21 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41f8b65b-0028-3c44-9c3c-d81644615d37 | 1.92326 | -50.81972 | 2026-09-16 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0cdd7107-73b3-3371-bc2e-877125de25a7 | -1.21349 | -47.89408 | 2026-09-16 04:55:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e03c61b6-ebfa-33d6-b500-dfc794a171e7 | 1.96838 | -50.93121 | 2026-09-16 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31a29eed-e640-3bae-a7c1-2b3744ab6c68 | 1.44381 | -50.6944 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a598c746-76c4-3389-abee-7531114e8689 | 1.18139 | -50.94811 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11d08b21-2494-34d6-a1af-d4573649381b | 2.70189 | -60.29644 | 2026-09-16 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c08205dc-f306-3b74-b3fc-59718d0f0af8 | 1.21948 | -50.78544 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8eadc4ec-5578-3b11-aa51-296e7e931cf9 | 1.27699 | -50.88525 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c57e8d3-04c7-3997-8d27-ff7ec2becec8 | 1.17461 | -50.94917 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de2751c4-3bb2-3098-9413-2bb64317cb94 | -1.33278 | -46.22098 | 2026-09-16 04:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3eec1ed6-f111-3a53-bb98-8972887c4ad5 | 1.96107 | -50.95078 | 2026-09-16 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32557c38-7eaf-3381-ad20-c4b78f782203 | 0.0912 | -51.06974 | 2026-09-16 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1d25530-36bd-3fff-893c-35c39bc437c3 | 2.71258 | -60.30053 | 2026-09-16 04:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19a7ec0b-cda1-35e2-97bb-7c938e862e7d | 2.18496 | -50.92397 | 2026-09-16 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1d1821f-dc2d-37a5-93b9-cf883656077b | 2.58512 | -60.30355 | 2026-09-16 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 30dd03ec-5b31-3014-bd7d-c1b349ba535f | 1.25234 | -51.01564 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df757168-55e2-3ca0-90f7-d244bfaea739 | 2.20565 | -50.89096 | 2026-09-16 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d13b61d-c581-3cbb-8866-94cf551b2a6c | 2.19338 | -50.93369 | 2026-09-16 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ff03649-697b-304d-93e2-16c037c8e448 | 2.21297 | -50.89351 | 2026-09-16 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3414bf31-8261-321e-9593-128ff4e0d12c | -0.00014 | -51.22564 | 2026-09-16 04:55:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02ba8466-8dcd-3281-93b3-2b39bd7efa73 | 4.29388 | -60.9633 | 2026-09-16 04:55:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e70f9e8e-f8c5-37c5-a1eb-6deff0f40c5f | 1.34697 | -50.63748 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3aef6781-e423-3d22-b606-41a2e0641769 | 4.74607 | -60.56765 | 2026-09-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fcd8a18-eaf7-36af-87db-e37f35ee69dd | -5.4631 | -60.22263 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaf70899-542e-3445-a9c2-8a2b23012fc0 | -3.69967 | -60.62037 | 2026-09-16 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71744982-d00c-3b8d-9709-2d2ac0cc7cc8 | -4.43448 | -55.71784 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d885c618-154e-331e-957a-0aca9d3a20c9 | -2.8892 | -50.42702 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6faf9df1-67d5-3e63-9898-97de38788d59 | -9.11455 | -45.73614 | 2026-09-16 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| caa5503d-cad8-3c83-a2d5-4ead60bf7b59 | -4.7176 | -48.31164 | 2026-09-16 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 793522b9-0a7d-3e94-920b-1172848cb1e5 | -3.73933 | -55.94174 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f7f3aed-fd5e-325d-89f1-38cd7d8dc537 | -8.79478 | -46.90837 | 2026-09-16 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d60ef97f-36c0-3ee7-b02d-d47820725919 | -3.70575 | -60.61185 | 2026-09-16 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61a01a77-0286-36b3-8aec-5b8d36b03917 | -4.55245 | -54.92266 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b67bc3c-7c15-3f05-bcc9-03ce3e09df99 | -6.11007 | -55.65516 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b4b210f-fd2e-3cae-9d25-d19600de03b0 | -2.90974 | -50.4132 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6c7763d-4eea-3cb4-918f-fafd610e8a9a | -3.73184 | -55.94445 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f827dd79-e575-3ffb-8726-a194a83e6563 | -2.10014 | -52.03946 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef64d55b-3c5f-3f48-8ff9-381dfb973b8b | -5.83369 | -52.09679 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 861ca6bf-6d3f-3254-8e3c-8b508c3e8c42 | -5.63454 | -51.69456 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2bb5ca3d-42e4-3567-b762-3b4e86f7dc5a | -2.91272 | -50.4179 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8aedd345-fb0f-38fe-9778-d262948bda5f | -5.15145 | -55.93563 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 15bc12a9-3b3c-3796-a11f-8c338559d620 | -4.46676 | -55.24961 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a22ed74-c3f7-336c-8515-fa733276efcc | -6.71858 | -58.80869 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 607e1a4f-6792-3466-b000-dbd152dd1737 | -6.11391 | -46.1029 | 2026-09-16 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57ca6dd2-298b-3f19-b938-4aa27466e689 | -2.57502 | -55.99537 | 2026-09-16 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a59cbe4-4aeb-3aa4-a90b-303db32ed213 | -6.27159 | -43.2799 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 803f81d6-fe32-3d3c-9749-a1870eb43f27 | -5.69146 | -52.29339 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8f4d5ac-3aff-32e7-94cb-bd36b91a8b9d | -4.43108 | -55.71732 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7492bdf-d8a2-396d-a723-559b64cab886 | -5.86025 | -51.94543 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a48ec394-0a80-3d0f-8213-b42068ec45e2 | -3.55068 | -58.6782 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab1e5251-76cd-3aaa-a8a5-50dd650d305b | -2.82467 | -51.3433 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eda26419-febc-3749-ae10-a93890f56a92 | -3.02189 | -51.33712 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| daa8113a-1be6-3dc5-bb41-c9add13bafee | -3.40054 | -50.75856 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4f57616-aad8-3230-8979-22b76c867fcd | -3.76373 | -51.80437 | 2026-09-16 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e126345-bf05-33b1-9808-33209d5533b4 | -3.886 | -58.74734 | 2026-09-16 04:57:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22260d3d-7996-33b8-8644-d6fd5904ec41 | -5.6197 | -45.24685 | 2026-09-16 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8eac9f72-c1a4-3ddf-ac87-819327751ad1 | -6.09999 | -57.68582 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94b212c6-4aa7-335c-9922-30964bfa14f6 | -5.62013 | -45.24376 | 2026-09-16 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb4177b6-b91e-34d4-b9d2-0a08abb7e65e | -6.33398 | -62.68959 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e3cc057-3698-350b-91b4-fc8f1ce737e5 | -8.26136 | -44.81974 | 2026-09-16 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3e5122d-5de5-3b1a-b6ac-f926c2810cce | -8.95529 | -44.39809 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd2273e7-e7d1-3846-a731-244064325b07 | -3.84504 | -59.33582 | 2026-09-16 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57731cb1-abe7-397b-ad40-a74f1cf55d53 | -6.79502 | -58.78897 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README34.md)
