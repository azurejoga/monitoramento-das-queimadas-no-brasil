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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9393e59-dc2d-3374-b634-b6fbe5a894d5 | -5.39427 | -37.70256 | 2025-10-02 04:27:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2f3089db-a7fc-3e06-978e-d95964fe78d3 | -5.34175 | -42.65978 | 2025-10-02 04:27:00 | NPP-375D | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10cdb534-887c-38b5-8c4e-8b6f2b749620 | -5.92152 | -44.86081 | 2025-10-02 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a6e8aa7c-a4b4-374d-9698-eb19027e720d | -1.57893 | -47.31074 | 2025-10-02 04:27:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7db2a46d-230e-3093-af63-bf88c4d9666f | -6.29391 | -42.48112 | 2025-10-02 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3cab1189-d12c-35d5-bb27-01bfb0ba5018 | -6.22489 | -42.96683 | 2025-10-02 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b60637d5-0905-300b-b146-4729910481a3 | -2.59301 | -48.12293 | 2025-10-02 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a75182c8-e52f-3668-98c6-f60e60240e39 | -4.37662 | -48.71905 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb0127f5-97f5-3b6d-bfc5-2303c17409ee | -5.98055 | -44.5915 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a6e8bac-a086-3ba2-99d9-dcb6f5a767eb | -5.18999 | -45.07335 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9845c675-dc3a-3f0d-9dc6-5ccf6eca7168 | -5.74605 | -42.86364 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4b5fb736-9be4-31dc-9971-d4df739b763d | -5.91656 | -44.91518 | 2025-10-02 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ddcf71b-1232-37aa-ab01-dec28f0b0fb5 | -3.82308 | -49.09599 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3a2b2c70-2624-3537-8df1-5844976ce938 | -3.78379 | -48.62957 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4880ed6-4922-3e85-ad3b-b4644cc4d638 | -6.08389 | -42.49468 | 2025-10-02 04:27:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 73a7479b-fb35-32e5-89d6-7dca296d9eb8 | -5.1015 | -43.7999 | 2025-10-02 04:27:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53c1cac0-e558-30f3-ae98-8533d230fff8 | -5.98509 | -44.58469 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c6a1864-094e-32e2-8085-609a7479993d | -4.1488 | -44.85731 | 2025-10-02 04:27:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87ac24df-006a-3a34-8d22-ca39b66b2ef9 | -5.18719 | -45.06931 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c8c1468f-171c-34fe-9afc-fd8e43f0af87 | -4.42641 | -47.75536 | 2025-10-02 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5994addc-4f83-38fc-97e7-be68ab1d53ca | -4.83539 | -43.51316 | 2025-10-02 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9704e427-f8ae-3863-893d-56737f7aa7e3 | -3.49729 | -50.27398 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ad8cbd61-08b8-3e4b-bad8-28b8aa1d40d7 | -3.81317 | -47.57335 | 2025-10-02 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a5d3983d-13e9-3cc0-ab84-5571b1a22c63 | -5.98904 | -43.99751 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ce0a992-2c99-303b-92b0-c6abb5c30192 | -5.8281 | -44.98971 | 2025-10-02 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccfd57a5-11cd-382c-80a5-beacf40d9027 | -5.7918 | -45.73689 | 2025-10-02 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9aa71522-63b8-326a-b641-91c4f645c0d0 | -5.38272 | -42.85125 | 2025-10-02 04:27:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 28af6fd3-e6a8-3216-a19e-99703c00bbb7 | -5.72061 | -42.68488 | 2025-10-02 04:27:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 095a8d03-16b5-34b1-824a-ff59b3a6f40d | -5.27466 | -43.16684 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9205e529-0a68-3f9f-9f91-a2ab5a2b71ca | -3.81484 | -47.585 | 2025-10-02 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bef58e6e-8ff1-31ef-917c-0df2a8ce0878 | -4.44915 | -43.23706 | 2025-10-02 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77743c92-0420-32ef-9382-3c5bc7700844 | -3.09578 | -47.01609 | 2025-10-02 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bf68203-983d-3739-9942-269f20ab8ac8 | -3.78737 | -48.63014 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96d5c9f3-76a3-3ed3-bf80-3a48ff1857df | -6.10483 | -42.6834 | 2025-10-02 04:27:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8126aa57-1804-3375-b03c-8f2a27e6dbc7 | -3.37788 | -52.72018 | 2025-10-02 04:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa271ea7-fd87-3f40-8ec3-153dbe468e47 | -3.92132 | -41.57424 | 2025-10-02 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e5c4481a-d889-3228-b4df-5a57d073a408 | -3.09636 | -47.01248 | 2025-10-02 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6df0b52-939d-33ab-ad9c-82135eb238b8 | -5.98567 | -44.60352 | 2025-10-02 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23389aba-d3b7-32e3-b516-d441ace607d2 | -3.34275 | -43.19573 | 2025-10-02 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ab43fbff-e963-381a-9656-3689b6bc6bf4 | -4.05303 | -49.08213 | 2025-10-02 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9127c8e-f604-3ad9-9f16-0e281e08fd4d | -5.239 | -43.74559 | 2025-10-02 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 89166f36-5284-3c64-bb35-ae1847601fdd | -5.33432 | -43.76023 | 2025-10-02 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a23ab7df-e018-3e20-bf3e-7b41c591827b | -3.09909 | -51.35594 | 2025-10-02 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69234d64-1e3b-39a7-835b-e775fd121de1 | -5.4613 | -42.84971 | 2025-10-02 04:27:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e9e8785-b63c-3308-821a-296e47901207 | -5.35779 | -45.96031 | 2025-10-02 04:27:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9f7ddae-20b5-37b2-8ae4-d1d923807571 | -4.64928 | -47.95855 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2f7da37-4e8c-3b00-b4b3-daf52adc6867 | -3.40302 | -46.90292 | 2025-10-02 04:27:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51ba6fdc-966b-39a3-9f53-4fcd8c2c5c88 | -5.42954 | -44.07333 | 2025-10-02 04:27:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b3ae092-aa22-3a18-b0e6-e615bf014aad | -4.11259 | -47.93368 | 2025-10-02 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ef5c85c-0953-37e7-91b9-bd699db8fe7f | -5.67754 | -45.32529 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 10ff8228-92f5-3a38-a304-210d625adc07 | -5.5503 | -41.57703 | 2025-10-02 04:27:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1f3bc03d-5404-37ad-bdc2-0af7e3a0dee6 | -5.4893 | -42.76299 | 2025-10-02 04:27:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 114d096d-fed7-343a-997f-587d73f78c5c | -3.81141 | -47.58445 | 2025-10-02 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a680132e-adf3-358a-963b-146051080d90 | -3.2751 | -43.53397 | 2025-10-02 04:27:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2ac7b36-c0d3-31a2-85e7-4adb6dfc6448 | -5.6742 | -45.32476 | 2025-10-02 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 3630a378-f1b9-334e-aeee-893bbb89e316 | -4.4057 | -46.33265 | 2025-10-02 04:27:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e82d83ad-230a-3a93-8943-148ac67fe46b | -4.25434 | -48.55611 | 2025-10-02 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a277c0ac-3fc3-36ba-9b84-550e875b5cfe | -5.31015 | -45.75049 | 2025-10-02 04:27:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68197e98-c50a-3d8a-8f90-7fb8b2abb5ca | -3.78645 | -48.62745 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0fd5f0d-ec13-36ed-a098-63cbeb49b45c | -5.70329 | -42.69971 | 2025-10-02 04:27:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 39813404-9bc9-3674-88f4-b9b33b70e07a | -4.93428 | -43.73678 | 2025-10-02 04:27:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc857c7c-63ab-3be7-a65e-f37527c1e3d4 | -5.46193 | -42.84549 | 2025-10-02 04:27:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cff1612c-f2c2-395c-8707-c6251b0ee460 | -5.41264 | -41.32669 | 2025-10-02 04:27:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 404d9e05-267c-3f31-9c6f-06db6222d4b4 | 2.26673 | -50.72846 | 2025-10-02 04:27:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25f39758-36f5-37b8-a474-135f48ec653c | -3.38537 | -50.14651 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75aac530-fbb3-3f34-a52a-432449947cd8 | -5.27508 | -42.87559 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d8275997-73ad-3fa3-b174-46f3804b292f | -5.75703 | -42.86523 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e4eac92e-49c5-384d-9d2e-332cd6f121c3 | -5.69658 | -42.69417 | 2025-10-02 04:27:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d24058f1-c7a8-31c8-a758-fde6c80ed3c2 | -5.79568 | -45.73392 | 2025-10-02 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2469f1b2-3d96-3e99-a25a-3247ba233005 | -3.17433 | -42.95546 | 2025-10-02 04:27:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c55c5a2-7da3-3fdc-8009-a8be09d368c8 | -0.90034 | -47.54527 | 2025-10-02 04:27:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e60edd8-09d9-30e0-a346-eca8148db01e | -5.84126 | -42.79805 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0f5e5281-3764-3abf-a744-e1344ac8d962 | -3.48685 | -50.08933 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6cd29005-10e0-3535-8033-b60a6acb9d59 | -5.99021 | -44.59671 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5bc828c5-d134-333c-9b38-c7aac5c673be | -5.82548 | -42.8525 | 2025-10-02 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f89f8ddb-241c-37a0-b95d-6eba17a54977 | -5.79831 | -43.07991 | 2025-10-02 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e4e891ac-99d7-305a-87e2-59dc7f68bb18 | -5.18026 | -42.83668 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0402d357-1ea6-3902-9441-607c5ce3f6df | -4.42582 | -47.75908 | 2025-10-02 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f7bdff05-9334-3f9f-b555-a029a7ba2ea0 | -5.2808 | -42.7642 | 2025-10-02 04:27:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 725fafe5-e522-3e6a-ace3-b6edfa2a28c4 | -5.49014 | -42.73247 | 2025-10-02 04:27:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3b7943e7-69aa-32b1-a79f-5e8cb30b5942 | -3.34685 | -43.19239 | 2025-10-02 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f279c999-4d9c-3e17-9c85-c23ec0de0ce8 | -3.69178 | -49.56424 | 2025-10-02 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c315c1e0-6656-3200-b8f1-cdc81a6db11c | -6.1002 | -43.4409 | 2025-10-02 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d665f47-6a94-3ffa-98d1-96cc5d59afa4 | -5.45574 | -43.94981 | 2025-10-02 04:27:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| caf21154-2078-3eef-a64d-e43b26e59a59 | -5.69721 | -42.68991 | 2025-10-02 04:27:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7ef574cb-4db9-3a52-b113-7536780a8ae8 | -3.46573 | -50.09597 | 2025-10-02 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10cf2ea7-3234-32bb-849d-46746828e61e | -3.92591 | -41.57006 | 2025-10-02 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 78126f61-d487-310d-ac1d-8f665f57510a | -5.89138 | -43.20338 | 2025-10-02 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1a63dd74-a681-3815-9622-4d29d44f4512 | -3.95153 | -41.5954 | 2025-10-02 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 08f1169b-473c-3167-a608-10dea144475f | -5.99191 | -44.58573 | 2025-10-02 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a60a38cb-e9c9-36c7-afb4-c6ea3fa6c707 | -5.27872 | -42.87614 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 90b156d6-323b-3cc3-a298-6f996b0d3ccc | 2.26555 | -50.73029 | 2025-10-02 04:27:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0027e8a-943a-32d6-a90c-c8b1aaa104fa | -5.41187 | -41.33181 | 2025-10-02 04:27:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8cc3b00f-68fe-33e0-9e70-ebf95be4b722 | -4.57744 | -43.969 | 2025-10-02 04:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5adf0be0-1378-32c2-8148-e26926252f2f | -5.24584 | -42.89688 | 2025-10-02 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 779397ee-a089-325f-8691-3e6d83855d3c | -5.72006 | -42.45926 | 2025-10-02 04:27:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dfbd2ff5-c03e-30af-91ef-e23e1f9dec11 | -4.58112 | -45.61139 | 2025-10-02 04:27:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 978be71e-709f-3858-ada3-6ed7f791a480 | -6.10021 | -42.4881 | 2025-10-02 04:27:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a2111b84-71c1-3848-ac9d-3f79a9149741 | -3.41365 | -48.88539 | 2025-10-02 04:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b0d1175-06d9-3d5e-a79d-6f60576b0688 | -3.89142 | -42.52489 | 2025-10-02 04:27:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README58.md)
