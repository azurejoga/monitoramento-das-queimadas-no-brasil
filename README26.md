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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d38d3d2-e667-36a6-b92a-7f238d258805 | -7.1492 | -41.71082 | 2025-10-14 04:23:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e1b0fbd6-36a8-30f8-abec-2f03feae6ebe | -6.29525 | -42.99913 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 91b953ce-25a9-3081-a043-34d3583f4cb0 | -5.87472 | -42.82745 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 05af5a3c-2e17-3ce9-a4a1-ce525105a03e | 0.3926 | -51.03362 | 2025-10-14 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc738fae-d763-3cea-a4cc-ac0f37022194 | -5.40327 | -46.02089 | 2025-10-14 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9577b611-27f9-31bf-a03a-f28fff8d4827 | -4.05567 | -47.25085 | 2025-10-14 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1fc9245-2f9c-32ad-86b2-46d4169ccdd3 | -4.67286 | -43.13956 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea91366c-47b5-3b42-84e0-7ef6e7e4f0e5 | -1.89647 | -51.01291 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 326966dd-2bfb-384f-b18b-04512b7990e9 | -4.66353 | -43.13018 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5a88c49c-f776-3102-b37d-60f81de2cc1f | -3.29808 | -51.59972 | 2025-10-14 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49e8028d-8076-3427-a83e-a25c6a9ca0a3 | -5.97532 | -44.93003 | 2025-10-14 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8971911-249a-33d6-98e7-bb36190a6263 | -5.59519 | -42.5818 | 2025-10-14 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7d494d6b-84bd-3155-b9af-a7b2908dc8b1 | -4.8326 | -43.20338 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc8fe377-0e20-3888-a5bc-2973f6251365 | -5.31332 | -42.90331 | 2025-10-14 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ce3dee55-1f89-300d-ae9b-54e14fa84a79 | -3.22611 | -50.05318 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55e1e5fc-9678-3aad-b750-30ace6f4ec83 | -2.98588 | -50.29294 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d01b1c9-63eb-36ef-8977-11b8546ecc44 | -5.25755 | -43.21698 | 2025-10-14 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee6f8a43-de2f-36d6-a299-6e1002940518 | -5.26106 | -43.21753 | 2025-10-14 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a1e2711-bfc0-3652-aeec-2816b6d7be18 | -2.87316 | -50.73223 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96328165-093a-3a09-bab4-9afeb3b07427 | -6.02917 | -43.4003 | 2025-10-14 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6771a4f0-3d4c-3b43-8f92-d6463ea8035c | -5.88211 | -42.87489 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a6e76394-f040-343c-b1aa-2467d376f8ed | -5.49738 | -43.06954 | 2025-10-14 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 521b1321-cdac-3b58-9519-290a4651a155 | -6.53627 | -43.56092 | 2025-10-14 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ccef8aab-8876-3389-94fa-43dd2082a465 | -6.12454 | -44.94976 | 2025-10-14 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c0b0fc04-173f-3bf5-a0d6-d14b64602d10 | -6.29795 | -42.99195 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52aa573e-47c8-3ee4-8b89-5282e1751d31 | -4.74123 | -45.65104 | 2025-10-14 04:23:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc36119d-8bdc-3c82-8160-06ba24a20195 | -4.23797 | -40.35711 | 2025-10-14 04:23:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 322e6489-e54d-3a42-9107-59f58d010edd | -3.47844 | -43.30422 | 2025-10-14 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b550dba9-c8ea-3a7c-ae7f-39965c06897d | -5.56398 | -41.3236 | 2025-10-14 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2b16ee3-ac0e-31df-8e86-abd58ee44ab0 | -5.72045 | -44.54203 | 2025-10-14 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c203999-6e26-3914-bd50-c0e7ed549e74 | -5.11152 | -43.20321 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ff3df692-a48c-3934-895e-b753473a1a47 | -4.90424 | -45.50045 | 2025-10-14 04:23:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 485c7c4e-8e7b-371c-8c1c-10cc6a0f6779 | -4.69278 | -43.12663 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05a4c54b-25eb-3ffc-82f9-dc0bc193bc26 | -5.2063 | -45.48045 | 2025-10-14 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b63ecbb6-da35-39c1-b107-d71bbf6ad313 | -5.91436 | -42.81981 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 06c7bd05-d7cc-30cd-b203-e2862ec915c7 | -3.26297 | -40.68896 | 2025-10-14 04:23:00 | NOAA-20 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 80e7fd21-6d0f-3ee7-baf5-6a0d7842ed3b | -6.15343 | -41.76885 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4e8c8f95-9df0-3118-af91-e7dc7eca087d | -5.87567 | -42.88154 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2f3eda74-2a3c-3c66-bf99-17f6092c0d69 | -5.49384 | -43.06899 | 2025-10-14 04:23:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 73c97fcb-7d95-3116-821b-aea6ef271acc | -3.2751 | -50.05068 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 968cd6ec-1528-3d11-a109-16b73f6b06e9 | -4.282 | -48.57216 | 2025-10-14 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7313d72c-21f8-3184-a301-70f8ac23270e | -3.13711 | -50.20689 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1da237f3-c57d-3f95-aae4-6d78a044151d | -4.75 | -45.89582 | 2025-10-14 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f116c06-ca05-3ed4-8f9f-aea1d6888fbe | -6.83526 | -42.78271 | 2025-10-14 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b1a62544-e2d4-3a7c-9a77-d0dd0bf7eb7f | -3.06505 | -49.40895 | 2025-10-14 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cebafb69-3b42-344a-8846-7a7eaa458f35 | -3.54133 | -49.43637 | 2025-10-14 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57eb2060-b6d7-3f56-ab0b-906b8c55ac18 | -5.71809 | -47.4302 | 2025-10-14 04:23:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35c9c319-70b3-3d64-9aa0-c65fef60e665 | -4.86149 | -49.47749 | 2025-10-14 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 709283f5-a529-321a-a3a5-8cba32163143 | -4.85011 | -43.20602 | 2025-10-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dddbe6d-a9d4-3a07-9906-3c79e46ff65e | -4.87006 | -47.33677 | 2025-10-14 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7645e464-f264-3322-8bfc-a5469570e697 | -5.31085 | -45.52898 | 2025-10-14 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a4b3317-7c70-36dd-8939-94a6746fbb0d | -3.09392 | -51.29901 | 2025-10-14 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa3ba08b-c0df-385d-a53c-608383ad368b | -7.08754 | -41.95703 | 2025-10-14 04:23:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a7c78506-095d-3261-a16e-95dc14f96e27 | -7.3966 | -39.7872 | 2025-10-14 04:23:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f7abadb9-680f-368f-a4ea-38fa68f0b381 | -4.91934 | -41.5341 | 2025-10-14 04:23:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 213d7293-28b2-3ec9-9ab5-9fa45441c711 | -3.39441 | -50.13351 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d67488d8-4f95-3a2e-b36b-6d9df43f4b23 | -5.64866 | -43.60997 | 2025-10-14 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a7f61fa1-3ab0-3698-84bd-88d96de1afc8 | -6.18639 | -41.74682 | 2025-10-14 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2c7683ad-bf28-3b39-a985-af8fa563833d | 0.40222 | -51.03662 | 2025-10-14 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3d0aaaa-bbd2-3b28-b927-5361da6ef4ff | -4.22916 | -43.01512 | 2025-10-14 04:23:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86bd1fee-9451-341b-bcf4-f45f381046b5 | -4.62178 | -45.78391 | 2025-10-14 04:23:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61806284-f1c1-306a-a1d3-67d9015f1b18 | -3.13143 | -50.21659 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1e7412b6-f689-38d8-a751-edb323ec4404 | -4.62341 | -45.77357 | 2025-10-14 04:23:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f7e856c-cdf8-3aaa-b05d-83a037cc92ef | -5.85111 | -46.45311 | 2025-10-14 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd1bf8a7-90a5-3a18-b021-149c6d0a8f8c | -4.7419 | -44.43552 | 2025-10-14 04:23:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e1f6650-d62f-3402-b9a7-70b9c00b199b | -5.90405 | -42.83941 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3e5f9695-9858-3c22-9283-a9b090ae6a0a | -4.09884 | -43.22945 | 2025-10-14 04:23:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b282120-2d60-3336-a1e7-31997219d168 | -5.15034 | -46.11448 | 2025-10-14 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a78c192c-fb5d-3930-8ae6-1d40270bca4c | -5.54609 | -46.38346 | 2025-10-14 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bee07fd-d2d2-3b8c-83af-7e0bca476ea4 | -3.14398 | -50.215 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07db1ae3-00b5-3b8e-96f9-2e45b2b3d205 | -3.05456 | -40.81572 | 2025-10-14 04:23:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2ab9e2cd-cbba-352b-ab80-0c8799018934 | -5.22509 | -50.95692 | 2025-10-14 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ebeefe3-a323-37b3-a629-915532b1cca4 | -5.74012 | -40.76695 | 2025-10-14 04:23:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b9cf7165-402c-3d95-b718-f408e86eb866 | -3.0995 | -50.38711 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3663e64-210e-34b5-b20b-211bf1ac03a7 | -5.15128 | -46.26017 | 2025-10-14 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c05c8fd-ff24-3ff7-ba21-3249b93bade8 | -5.53577 | -46.49184 | 2025-10-14 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f07367c-7d59-3f93-8733-160f7dc5273b | -5.8785 | -42.8744 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a9cef4c7-0712-3e0c-a0bb-08913340b40c | -5.55486 | -46.95054 | 2025-10-14 04:23:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc1ac4fa-729a-37e5-87d0-a206628430c3 | -1.9556 | -50.81026 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8f73cb08-8238-3192-b14a-b90f3079d223 | -5.87926 | -42.88209 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3c0e2492-bd72-304f-b0a4-588ea884e9fa | -5.90702 | -42.84411 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 21fd6f59-52e3-3d3b-b5c7-30a0ac1437f7 | -2.53183 | -47.81015 | 2025-10-14 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40810549-107d-3c2c-9907-55467df7bc6b | -5.30495 | -42.91022 | 2025-10-14 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bff618db-cd18-3df9-93cb-dba9118b6e3a | -5.78998 | -43.89393 | 2025-10-14 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 070bbffc-a4fb-34eb-ba0b-339bd96d8c68 | -5.59703 | -42.56715 | 2025-10-14 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7d274c08-3cee-3f25-ac89-c574d8209fb0 | -4.74399 | -45.65499 | 2025-10-14 04:23:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83d32c25-337e-3ec2-83a3-38c766b1f997 | -3.88981 | -44.90951 | 2025-10-14 04:23:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c866639c-b903-341b-a522-3717400aba2f | -3.12912 | -50.20564 | 2025-10-14 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89f9430c-ff1a-3646-90bb-92536cfac4f4 | -6.32118 | -43.89977 | 2025-10-14 04:23:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34d3f290-184d-3bdf-84ba-4925471a5320 | -6.16226 | -43.75195 | 2025-10-14 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 692e760b-8997-36d0-8c23-79fb1ad068cf | -5.19232 | -45.39688 | 2025-10-14 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d21b0fd1-94d0-30da-8ccb-20ac11e67751 | -5.67971 | -42.68532 | 2025-10-14 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6cadbccb-a921-3e3b-a994-a4ab38a9a24e | -6.16514 | -43.75627 | 2025-10-14 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8e32d9a-7852-34fd-858a-de051a8d3ba5 | -5.88173 | -42.86555 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bab21be7-88f6-314b-b989-8352cbdc2d3f | -5.87427 | -42.87801 | 2025-10-14 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1d7c1f13-a68b-3a2c-b008-79a246e1b9fe | -4.84378 | -42.77832 | 2025-10-14 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 7a6f3bad-bbb8-3e35-8eff-9f80a753e485 | -5.30557 | -42.9062 | 2025-10-14 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 908d9a9f-b75b-3aa5-a0d3-717a7a2782b5 | -3.43941 | -50.24888 | 2025-10-14 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 936a4377-27be-381e-aaf1-bf8159527cec | -2.7232 | -49.58527 | 2025-10-14 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc5ce5f3-144c-399b-bfad-294ceb392847 | -4.24626 | -42.97354 | 2025-10-14 04:23:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README27.md)
