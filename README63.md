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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4097615e-0b7d-36e7-ad13-63afe88cceb9 | -9.1277 | -51.30185 | 2025-10-27 05:01:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be26c25b-142d-3d5b-9ee1-0e6caac93906 | -12.51035 | -44.32975 | 2025-10-27 05:01:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9241eae-4944-3d03-ad18-e9693e0d4f96 | -6.14278 | -43.13335 | 2025-10-27 05:01:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bcc2c0dd-d5f9-30c3-942f-e5250c4c024c | -10.36095 | -47.17918 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a2c9e09f-1355-381b-b8fd-c8acf585638a | -7.33118 | -47.13983 | 2025-10-27 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| de91a906-c0fe-3b36-a139-55b8cc333706 | -8.52942 | -47.19613 | 2025-10-27 05:01:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0f48b81-bf88-327a-aec5-9c6cf25fe96b | -7.76223 | -45.40147 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f6eb20e-0929-391e-a7e5-33b599015218 | -8.45957 | -51.08727 | 2025-10-27 05:01:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d6347ff-b572-3536-a740-cdd2eb878ce9 | -6.88169 | -45.15178 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32e62cc8-3978-3d43-9f78-ee96c50e51fd | -8.32858 | -46.16732 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1497026-aedc-3d1c-9d53-37b395092cb0 | -8.53436 | -45.56342 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3aa04ad-49bf-3436-b80e-5d9201dde46a | -10.74982 | -44.20211 | 2025-10-27 05:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 071a4c13-7156-3cea-92ba-4991bd77bfe9 | -12.06984 | -47.99529 | 2025-10-27 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da28ff07-c690-3e4a-b0b1-61d8ca60ccc0 | -7.39554 | -45.13112 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c705289e-e350-3400-ac54-983a636cbeb2 | -8.35775 | -46.15682 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7a8ed28-ef2c-3adf-baae-1c464512efb2 | -9.5743 | -46.90107 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5f4cfc42-b255-374d-92f6-deb75f5fc19b | -8.741 | -49.61293 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e24be4ac-359f-3af2-803f-2d3b063afa06 | -7.83998 | -46.46169 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8963ea4b-e060-32f4-8634-97618b219540 | -12.33288 | -47.48003 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1e786639-8481-3c23-89d3-d2fed04d6c98 | -8.32231 | -46.17481 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0692a19-70f2-371c-9a70-ad2a7ae1f9d4 | -6.9634 | -49.40747 | 2025-10-27 05:01:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82437768-327e-34d3-a0e7-7fd5a23a0637 | -7.97691 | -45.46922 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ac31e12c-db45-3589-8a1d-6e593284edab | -4.96755 | -56.26879 | 2025-10-27 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a734f82e-fec4-3bee-b96a-caeb0a702fa4 | -9.26404 | -45.60035 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e223ebaa-0809-3e01-a1c0-0cd123b5e652 | -8.2155 | -46.94146 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50fb9223-625a-3a3f-8763-744b4876183f | -11.79873 | -52.49792 | 2025-10-27 05:01:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 563df924-3aee-3d53-bb8a-7b8fe19ef941 | -7.9597 | -45.47538 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 54aaed0c-66f8-3e45-870b-4b38467dd15c | -12.05208 | -46.38712 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8af6e193-ef92-3d61-a685-00aaa35534f6 | -7.82804 | -46.43748 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8a3d8bf4-f5f2-384f-977d-7c7e8f640948 | -12.32592 | -47.48927 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c52de2cf-aee0-39e5-8932-4cf6f32068c1 | -10.64372 | -47.9443 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 467eb70e-edba-3960-9e2c-73e929104a8a | -12.08804 | -46.40309 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81f68e09-09eb-30f6-a994-17e077722094 | -11.91316 | -43.82241 | 2025-10-27 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 673c8d9b-2dca-397e-8cc3-46edd6077543 | -12.5047 | -44.32583 | 2025-10-27 05:01:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05c98a27-2cb1-314e-bcd5-069190051290 | -10.20921 | -52.66538 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a9244de-2c7d-384f-b2ea-0c296ff899fa | -10.35674 | -47.17287 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b101a057-947d-3b47-a01c-7baa38b6ee00 | -7.85163 | -46.45127 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72e98d5e-6101-3efe-93cf-8082590c55d6 | -7.87447 | -47.2519 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dca59eba-ae4e-305a-94c3-b298ed426297 | -7.43012 | -41.87173 | 2025-10-27 05:01:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 79c78e25-34a0-383a-8a70-df3dd276f18c | -7.25086 | -44.96177 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2dbd0fe-cdcb-3b3f-80a0-06530871d987 | -6.89043 | -43.57737 | 2025-10-27 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 527f96d8-c994-32ca-8937-9036ee4eadca | -11.05484 | -49.90311 | 2025-10-27 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffc79e73-edae-33e2-b391-a6e6f103bf9b | -11.42143 | -46.08956 | 2025-10-27 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b3b1d36-476c-38f1-b8b0-04bef0756972 | -8.02685 | -46.76194 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2c20588a-da8a-34b3-8662-9f3927b9cfd5 | -10.64775 | -57.34385 | 2025-10-27 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e5133fd6-860f-3b97-923d-1895594f09d6 | -6.887 | -43.57878 | 2025-10-27 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8b3d19ea-3145-348c-9df5-ca21f98a304c | -8.31083 | -46.18218 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 509c76c2-53ad-3412-8b54-96323ad32db1 | -5.82415 | -53.45358 | 2025-10-27 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bf4788f9-5ee5-3b85-abf6-681c72209d68 | -7.82612 | -46.48818 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5aefe8eb-c00d-35d4-8b6f-ee17f64577b6 | -5.71454 | -49.3107 | 2025-10-27 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cda30f5f-9b00-365b-a29d-f4304c4994ea | -6.88759 | -43.57431 | 2025-10-27 05:01:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f5e7b441-9df5-3e30-9d69-fc33fe517f1a | -11.43841 | -54.08929 | 2025-10-27 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7de51fcf-b044-3058-8035-0ca59760a274 | -7.84627 | -46.41649 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9bb9431e-9422-36a6-be3d-309c6b9629e3 | -5.6029 | -47.10254 | 2025-10-27 05:01:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c2ef910-f2f9-3eda-9048-1301aca99fdd | -6.88355 | -45.15671 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d040449f-a412-3271-837d-5fc9635e785c | -10.32884 | -47.15086 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51767a81-f90f-3984-8b34-4287137882a9 | -6.87397 | -45.16746 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 751ed886-4ba2-315e-9dd3-a0ec7fe72952 | -8.63186 | -54.89304 | 2025-10-27 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2650a3ee-ee3f-320f-9e6f-14c7348267c4 | -10.21683 | -52.66252 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d0f20b8-461d-31e5-8439-e230ed171186 | -7.97648 | -45.47239 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ccf18b6b-adcd-35d3-9162-7b58a637f51c | -12.28208 | -43.75885 | 2025-10-27 05:01:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 034d98c8-5b20-3506-a3e2-a4588ed28f1f | -7.77302 | -45.40252 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bbd1f03-0caf-3006-b796-6c2becb458a6 | -11.63046 | -54.58064 | 2025-10-27 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b40b940-02db-305c-95f5-602c3e519cc6 | -9.26356 | -45.6039 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8e2f13f-4826-3755-bf53-c4c529f624e1 | -10.21743 | -52.65857 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3037d402-f619-3b9e-9980-508990e26073 | -6.89905 | -52.19419 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d077bef-db1a-3ab0-8681-b3eb9d366fbc | -7.83612 | -46.4894 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 5e78d26c-fce4-3e09-ba29-f6177457e708 | -7.83457 | -46.5005 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6b9e5fd4-4b7c-3a51-adb5-9c4124745478 | -10.36023 | -47.1847 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 5eb59eb1-7a3c-3527-b491-553b2247d771 | -7.33771 | -48.48801 | 2025-10-27 05:01:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c32f86b-4134-3116-83e0-e86316f22493 | -7.91873 | -45.65806 | 2025-10-27 05:01:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2435aaf-7612-3f21-82ec-00e182abb181 | -8.12049 | -47.02909 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe464bf1-4d68-3bed-9698-3aa998b03396 | -8.5225 | -47.21125 | 2025-10-27 05:01:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5917ac92-70ed-34a9-af57-1f236b5e1257 | -7.85583 | -46.4577 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c4b44a74-95b6-3bce-8ee9-dc3e042e4304 | -8.69442 | -44.43452 | 2025-10-27 05:01:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0808115a-960d-35d9-abee-f2857f5a1b29 | -10.56459 | -47.8904 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e0404ea-869f-329f-8f7f-eb4a3584b6c2 | -8.21966 | -46.94715 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 128489f9-80c3-39b1-8384-f96e7906286e | -5.88739 | -49.37769 | 2025-10-27 05:01:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b88f92ad-034f-3ff3-8e98-864a6d595bfd | -6.8798 | -45.16505 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c68be7f-7f8a-3b8c-bbf4-797a9b57e21d | -7.77521 | -45.3866 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64f65eb1-036c-325c-b4c4-6b34af887b0b | -5.26809 | -50.97543 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a690b2ad-efe6-3dcf-a260-e2793ceb0c5f | -6.88611 | -45.15929 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70f08375-d8cb-3071-a0af-87d465c39c37 | -10.35893 | -47.18834 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 57cb6740-8e68-34e5-abcc-9f67e657efe6 | -7.83419 | -46.46672 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 959eb3be-fb64-3961-af43-e2d2134cc511 | -9.71754 | -48.92571 | 2025-10-27 05:01:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd8cfeb4-e7c4-359a-b0e6-c8cb840c3e29 | -10.83619 | -56.96083 | 2025-10-27 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66eac4da-47d8-3e64-954e-307bb025e58b | -9.12951 | -51.29993 | 2025-10-27 05:01:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0637b097-de29-3bf8-ad72-c5d2bdbb6147 | -11.42954 | -46.11176 | 2025-10-27 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac524b58-c93b-35b0-bcbb-c3f16da10e5a | -9.84323 | -52.26983 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2e697cd-be5e-3e62-ab6b-141da22d355b | -6.88075 | -45.15841 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 491d88e7-0a33-34bb-92b5-9f23a1b1b483 | -11.1492 | -57.52432 | 2025-10-27 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8cf4a6bb-4358-33d7-af5d-47b6e3c8fd08 | -9.56221 | -46.80587 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6bcc7c13-904d-376f-8a85-3155e9474f64 | -7.00073 | -46.99867 | 2025-10-27 05:01:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1cd4c35f-8239-3c74-95c7-5d4171b0ac94 | -7.24985 | -46.95764 | 2025-10-27 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6d5abe9-6d9e-3c59-a88c-ab41712affc2 | -7.76765 | -45.40184 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 914792c8-a07b-3007-b464-9e9358c44b72 | -10.54885 | -48.01141 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ee8bfd5b-648f-3744-a4bb-870a4eb478d3 | -8.23301 | -46.92281 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24ab4127-2bb5-3626-8bc4-0814ccf1d3f0 | -12.05228 | -46.60444 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34cc37f9-2683-3417-94c3-1dca8b3fee57 | -12.05245 | -46.38402 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce1e7704-1a7e-3c6e-a7ac-a08ca83654b4 | -7.84953 | -46.50255 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README64.md)
