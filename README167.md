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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87eaed18-8db2-3e23-8edc-1a54f7456c54 | -6.51317 | -55.41051 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee61cc47-d41e-3e45-9e53-959e1385cbd4 | -3.00109 | -54.11426 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 969e2293-352f-3ddc-821e-f01822b66453 | -5.2736 | -47.91766 | 2026-10-09 05:04:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98e5a3f8-4290-39cd-8361-5167b92b48f8 | -9.20856 | -60.87278 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b64c3c8-5b2e-38d9-aeb5-e78461072b9e | -8.58645 | -53.10166 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0192e682-980b-3f9d-ae33-b3ce85f37ffe | -7.08604 | -52.69098 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 557a03b0-e5f4-3047-931e-e30720f6bb3f | -6.11881 | -55.69753 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58948896-11c2-358e-a44e-15f3b4173ada | -3.98032 | -49.87085 | 2026-10-09 05:04:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26dc9751-ce0d-38be-ba74-eb905dce81d5 | -3.09471 | -53.93315 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c504e8e1-4b2d-34e2-ab0e-24bcafab1ed3 | -3.09392 | -53.96034 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c67d0e0-81fa-38ec-b83f-26b0e6b356d9 | -5.2828 | -47.90915 | 2026-10-09 05:04:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6546151-450b-3909-bdee-14f7914013f8 | -10.45939 | -47.85231 | 2026-10-09 05:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99a516a4-884b-3a5e-9def-46d4dec589f9 | -5.70742 | -53.4977 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b405eab-bda6-35af-81c0-99a491d3a5ae | -10.87267 | -44.80758 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7b2b144-4a6a-3a70-9569-968722d0b717 | -2.47315 | -58.08289 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5faf64c-954d-3925-aee6-66bdb260fe88 | -3.07519 | -54.25733 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 792057d5-c9a3-3678-9aa4-b34bd7d001d4 | -3.26779 | -54.02545 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| efe8a3c8-8dd4-32f3-b91f-b0bca9258fcf | -6.49082 | -55.31199 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e9e9df4-5d37-3f03-a5ad-5ecb357fd49d | -4.66822 | -56.21709 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22e540d8-d72c-30f9-9b0c-69c8ac6b67c1 | -3.08493 | -54.28691 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8101d194-799e-3a39-b753-9c5b7be8e2b1 | -3.25044 | -54.66581 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2eee2378-fb11-3602-82fb-d5a81c64407f | -5.88804 | -57.75459 | 2026-10-09 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a043a59-3aaa-3427-8f64-8b1badc9b802 | -2.94869 | -54.17041 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0d2d943-7ffc-3947-a2fb-8c5fd855fe15 | -3.10461 | -53.76103 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f9cb433-a8b8-3ee6-b637-9eb04ec066f4 | -6.86847 | -52.1853 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ff74210-e9af-3b8b-adf9-8a4aacad76b6 | -5.93084 | -51.82669 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e95059c3-5beb-32e1-bb49-401272271269 | -6.0066 | -53.49852 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ae45de7-a194-3789-9705-2726a8c51d91 | -2.92862 | -54.07203 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b10587ab-d3ab-32a6-9aab-71fd98002d01 | -6.48223 | -62.85877 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c15bf4f-3c47-354d-a812-51fb09d2ec6e | -3.57976 | -54.6816 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8eda072-a38a-31db-8bdf-f82d0f4e15da | -3.0971 | -53.7637 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cc6921f-90b9-3791-8eca-6659c26754f9 | -4.89792 | -54.98948 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a30b2ea1-5a26-3b8e-9863-94c49760e0d0 | -6.48846 | -55.29443 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1615045e-f1f5-3a8d-99e8-b3d59adb3b76 | -6.38898 | -55.27164 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74cd15a8-1199-3f6c-bd21-7d3cbcb456fc | -2.99572 | -54.14605 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a653b3d-a678-32f5-b88d-c8ebc2ac92ce | -6.44254 | -55.0511 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ad0d51d-adce-3692-a92b-cfccb4601c41 | -4.11245 | -54.62793 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b4690921-9bde-3329-95d6-8e2ce1aa97e7 | -6.20269 | -52.86381 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4e9ef3d-9eeb-3f33-9d39-59d52a295de0 | -3.70034 | -54.20543 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1c10a20-7e05-32f1-af1f-02dfa350d49c | -11.7561 | -44.92732 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b68cab9c-078d-3edc-a61c-856ce3a85f9a | -2.9993 | -54.05571 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a015440-2c6d-3a9a-9a63-48f1b15adc6f | -4.74243 | -54.61184 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ee71073-a438-3669-9901-d527ff1ea8f3 | -4.91635 | -55.85941 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4624a7fc-5ec4-3a33-af5a-0020687da2e8 | -6.50959 | -55.40991 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ab901b2-c1a9-3ea2-8c34-9801097ef277 | -4.32753 | -55.01501 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bdde506b-5748-3e2f-93e1-0d29d741d0c3 | -6.54272 | -56.04775 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8480c85e-c140-3f0e-a4d5-37436d553997 | -9.39777 | -48.99756 | 2026-10-09 05:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb916ece-0280-309e-bd67-2ce1f93e4e51 | -3.10919 | -53.93165 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 173a2076-c119-31b1-af06-744f0018dce4 | -10.87308 | -44.80443 | 2026-10-09 05:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c2aa3d89-6f12-3bb8-b61e-27a678aa348b | -6.16962 | -51.93589 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99a4c9c6-703b-3eb1-8e04-f4d4cb28be9d | -9.69255 | -58.08747 | 2026-10-09 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f70d090-141b-3830-894f-bad6fb8b8824 | -4.73242 | -55.66238 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbd812e7-51ba-3fc0-b96d-71dc113404f8 | -2.30983 | -57.98831 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 767ca55e-59e3-3c31-bf52-502e4621cfda | -2.98926 | -54.07382 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ea523e9-a66b-3b81-8708-508183bb220d | -4.52072 | -54.86486 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd922ecc-83f8-36b6-8d28-606f4f0ba4d5 | -5.10389 | -46.22115 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82bb676b-5a49-3f94-a9e6-f63e58c07550 | -4.562 | -54.21044 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdc23044-56be-3d91-8f25-d24e8d566a9e | -3.65805 | -54.28969 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e856d037-fd1a-3aa6-b58e-6ed67265a6b4 | -5.75814 | -43.84943 | 2026-10-09 05:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dfb32a6-dcbf-3a67-bd18-33a916039b23 | -2.99686 | -54.07108 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2ccd915-c424-3ca2-a526-b727246a964e | -4.94058 | -49.2165 | 2026-10-09 05:04:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9211e9fe-ff53-30b6-853f-15ccb350b2ff | -8.74243 | -45.14355 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 29f0f904-ce7e-3949-b462-ddcf00ffa956 | -3.10402 | -54.28099 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4edac95-10b0-3a8c-b57e-c477320f698d | -8.73256 | -45.14231 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d6ba682e-9b44-300a-a921-10cf445e0b42 | -3.00811 | -54.04531 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f82b00fa-daf6-39f0-932f-eadbf749ea1b | -5.99651 | -53.49694 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 074baa6a-967c-3668-91ff-411a350ec4ea | -2.93584 | -54.04953 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4343f75b-fee1-3335-9187-d1d33042ece4 | -3.78737 | -59.37817 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79aad14c-f74f-3d42-80ea-cf6a163743f5 | -11.27992 | -45.19601 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99c9b252-ebf7-3044-ae76-1b71a26fa240 | -6.12038 | -53.05816 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e12f9e4-9bb9-3ecf-901a-a8d83eb538ae | -8.73749 | -45.14295 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4f2d0020-caf4-38b5-8a58-22fecd11562e | -3.01747 | -54.05771 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e974d1c2-0429-37a8-b58b-1cbfab6c2662 | -3.74703 | -59.47596 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62965496-b124-39d8-aa7d-2077c0ee20f4 | -6.49277 | -55.29994 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 773f195e-e656-3bbe-b921-dbf74d6ac903 | -3.11592 | -54.16348 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 07291507-694c-3da5-aef4-e39dd1e5d58f | -4.37906 | -55.15699 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29ccaa2b-6204-3cab-95af-6d7a21a3a1f8 | -3.63378 | -60.62796 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7bb5d80-f223-3a79-aa73-48b4697f7e46 | -5.85708 | -53.45599 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ad93be6-1c10-3333-8bb6-7502c75cff96 | -8.98708 | -45.90012 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 237fb4f9-967e-3173-95d3-0faffa0b0f9e | -3.4273 | -54.0628 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0562d0ee-df5f-376c-98dd-ffe6709f8f7a | -6.57558 | -53.02707 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97954e0a-0112-3a71-81dd-c54c19248590 | -3.44405 | -59.55684 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d21097dc-a9f7-37a9-ba47-764f9a46b16f | -9.25843 | -60.8888 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17b0f3fc-c1b4-3dce-ad8a-2d6a3da5ac57 | -3.08481 | -54.26595 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdf12ae6-fe77-3359-948d-2b52a67e6bba | -3.01383 | -54.12419 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1307a846-c7fc-3860-81ee-13aad0aafcd6 | -3.55147 | -54.68682 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fb1426f8-2eec-3fdb-a76f-0acefd0e4caf | -6.44877 | -52.69963 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c86ee82e-46ce-3e95-b9f9-384a8d9cfd8a | -6.58059 | -53.01712 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 756fe6b3-fcd0-398b-b3ee-f7cb794cbb3d | -3.00307 | -54.09972 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 385f7fce-5297-304e-820b-0095e81aacdb | -6.22597 | -52.78192 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 914fe174-365a-3c93-a220-a0d84e1d4366 | -3.09349 | -53.94076 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1ae38f3-28ae-3ff9-9a12-0798c8273cef | -8.7039 | -62.40844 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1f6adc4-3576-31ed-83a3-16162429666b | -3.6697 | -60.60526 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a625fd9-03b1-3098-8d28-d1215226b537 | -3.0353 | -54.08025 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30f2549f-75bb-3ad0-86aa-d8d11451540b | -4.66058 | -56.21581 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9290841b-d65e-35ad-9352-463e6695513b | -3.08532 | -53.94728 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f4075d1-c300-3867-a19a-aebb69b719f3 | -7.51351 | -47.32807 | 2026-10-09 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43de9bde-6ac6-311e-9553-061fb5cd47b2 | -3.30703 | -54.67895 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b3604d0-27b7-3dba-b387-9d34acd12801 | -3.27556 | -53.99939 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fdb02c3d-2661-3f68-873b-c25d57222d3d | -6.33727 | -43.35146 | 2026-10-09 05:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README168.md)
