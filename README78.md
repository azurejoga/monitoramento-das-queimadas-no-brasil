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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40eb55f8-02be-31c5-92e4-a60c555d5b70 | -6.85142 | -41.70687 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dc8060bb-5d7b-37cd-9c4c-9966aa9a7333 | -6.85135 | -41.69218 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a10772ba-f0ef-34bd-94cb-da22e6d54934 | -6.84952 | -41.70553 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9b81a084-4ffd-3d66-9a58-2abf8158149a | -6.84827 | -41.68383 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3b29c4d4-13d2-3814-88a5-f776c57fa32d | -6.83544 | -41.80811 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7d570332-5ae3-3085-8fb5-ae3cdb4d1f45 | -6.83263 | -41.80444 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c9b6d0c5-5ec6-3d1f-91db-03f7008dd9b5 | -6.83205 | -41.80894 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6d9386a0-0c5e-30e5-b350-69d062016968 | -3.95454 | -41.49774 | 2024-10-07 04:51:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 868308ab-9340-3d95-967d-82bf51317ca9 | -3.94809 | -41.50094 | 2024-10-07 04:51:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9f0a9b66-317f-369f-9095-f0ce1cd27cf6 | -3.94344 | -41.49168 | 2024-10-07 04:51:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6d59e0d2-5c82-361f-87c5-b78653872674 | -3.94284 | -41.49585 | 2024-10-07 04:51:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| aa4774c1-3188-3aef-b4e3-9728178ec958 | -3.93758 | -41.49079 | 2024-10-07 04:51:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f21f0524-a04c-3055-95c4-ae67a5fb11c9 | -4.79427 | -42.75473 | 2024-10-07 04:51:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f44c6cb-6bef-3830-9666-18227fb87ae1 | -4.79292 | -42.75594 | 2024-10-07 04:51:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc428d01-da07-32c2-b6f1-3ea2e52a332d | -4.78883 | -42.75378 | 2024-10-07 04:51:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9d16925-fcf3-3e4c-a71e-b4b95e22fade | -5.64184 | -42.4161 | 2024-10-07 04:51:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 68bafcf4-bd8a-37a5-90dd-b41894ace9a5 | -6.29343 | -43.4587 | 2024-10-07 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 07663da6-bc8d-3782-bbff-a83baa75afa9 | -7.77892 | -43.08081 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a295b821-6880-336f-a0e9-49770c6da17e | -7.77844 | -43.0845 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4c0de1a2-a551-3641-b0d1-b46d8c37495d | -7.77795 | -43.08818 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| af2c6b00-c5a5-3973-baf5-c81be5e89330 | -7.73768 | -43.04836 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ae9fcad4-3066-3c65-a156-a7367cddfa1e | -7.73634 | -43.06827 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ec6264d6-b130-3cc2-992a-c7923a9afb11 | -7.73534 | -43.06646 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 02f4026b-3dfa-3e7c-96f5-f8933151e7ee | -7.73321 | -43.04951 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| de368128-cec9-36ef-a3eb-28f6d934d327 | -7.73271 | -43.05322 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| af953fbd-9247-3e54-a7c9-f102d74177a0 | -7.73221 | -43.05684 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4cda803d-8659-39f1-8ee0-a0b020e76ced | -7.73173 | -43.06041 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4a800411-0edd-3471-8696-2b1c7eda3ff9 | -7.73125 | -43.0639 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5a3f2578-8082-35b5-b7be-0cc41eb83083 | -7.73115 | -43.05494 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e545ead8-aaa7-37ba-8a0d-50f1af41236c | -7.73078 | -43.06731 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 63523594-5e10-3153-89f1-03c412bb016d | -7.73069 | -43.05851 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 55f70f5f-5413-3e08-b0c0-349f822bb1a0 | -7.73031 | -43.07073 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0afafee6-e13c-36a4-a321-7c5a20af33a0 | -7.73023 | -43.06204 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 55515813-f178-3cc2-a481-ff9ea71aa68a | -7.72978 | -43.06549 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9ec9b60c-0419-3c00-bd74-3fe0567e8498 | -7.72934 | -43.0689 | 2024-10-07 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 23a25fdb-2637-36b2-8767-dae4ba48a049 | -6.47132 | -43.21883 | 2024-10-07 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f465080a-3d3a-3526-99c0-0c6573780fcc | -6.47084 | -43.22235 | 2024-10-07 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ccc5d06-06fe-36cb-b455-4e6d067937b8 | -6.46591 | -43.21793 | 2024-10-07 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4d118e03-e132-329e-8275-3380252a6762 | -6.46542 | -43.2215 | 2024-10-07 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8a97e9cb-6660-3e65-aac8-b4a073f9c91a | -7.6492 | -42.49062 | 2024-10-07 04:51:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8d19781e-650a-3024-9c51-0f02a69d98df | -7.64866 | -42.49474 | 2024-10-07 04:51:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b7eb9eb1-0fa9-3b3f-ac27-59a05de12469 | -7.64759 | -42.50287 | 2024-10-07 04:51:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ed7eaa9d-9d03-38f2-b2c5-08b5a25398d2 | -7.64706 | -42.50691 | 2024-10-07 04:51:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 44abab0a-4779-3b44-a61a-9abfe3f3db52 | -7.64075 | -42.51009 | 2024-10-07 04:51:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| cd944817-8d98-3b36-af82-0c4a7c7110b2 | -7.63497 | -42.50926 | 2024-10-07 04:51:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 18b39668-73ed-38c1-a971-2054983e6307 | -7.63445 | -42.51326 | 2024-10-07 04:51:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e3c7a557-9252-38cd-897c-d80dd41db877 | -7.63392 | -42.51724 | 2024-10-07 04:51:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 4c29be60-1957-3972-99e7-48ff7168e5f8 | -7.6334 | -42.52122 | 2024-10-07 04:51:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 1335e7f4-5285-3eae-85d0-9267070e4c1d | -7.62943 | -42.41648 | 2024-10-07 04:51:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4194de15-d5c1-3203-a656-fdc6aa849f6f | -7.62762 | -42.52045 | 2024-10-07 04:51:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 395f7f98-48d5-31c7-b482-6785d47a4d16 | -7.62203 | -42.42743 | 2024-10-07 04:51:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 88f5077c-db6c-373c-a82d-6e337cb98088 | -7.62192 | -42.42806 | 2024-10-07 04:51:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a40aa176-50c6-3538-a8c1-76275b93da72 | -7.62149 | -42.43162 | 2024-10-07 04:51:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| bf667e36-59e5-341c-9545-59b0042bba28 | -7.6153 | -42.51934 | 2024-10-07 04:51:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 302facf7-8344-3231-844c-3c0c8a3958e2 | -7.30807 | -42.25049 | 2024-10-07 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8771818b-9aec-3e24-995c-a2c56de592bf | -7.30767 | -42.24897 | 2024-10-07 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5087e42c-b40a-344c-9785-2b7323d346aa | -7.30711 | -42.25335 | 2024-10-07 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a65ee374-6d44-3e33-b13e-a44f757027f7 | -7.3016 | -42.25424 | 2024-10-07 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 54406b6b-2a92-3008-b108-5698a011822d | -7.30069 | -42.25697 | 2024-10-07 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e6908add-3515-332a-b1c9-70e8f03aebc2 | -7.14545 | -42.63254 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6b99d91f-835c-303c-8b5e-98067a1c21c4 | -7.14514 | -42.61877 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f06ca429-0022-301f-a7b0-7f78aaf81bff | -7.14494 | -42.63647 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7978b9f1-652d-31ca-b56f-680badc6dd62 | -7.14301 | -42.63432 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 06c05b51-2942-3167-b334-7a12401ace71 | -7.14053 | -42.61003 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0aa82262-bbf3-339c-8062-cf95da24dc09 | -7.13999 | -42.614 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 959f4111-cdab-301e-852e-3c108f431b09 | -7.13677 | -42.63748 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 589c6318-bdaf-3955-8ba2-9aa13b560e9f | -7.11917 | -42.63894 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 76925119-ebe6-3455-b541-d4e210631cc8 | -7.11865 | -42.64279 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9cd13fc7-7f13-3d9d-baf8-17fff71e587a | -4.26833 | -43.73534 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 00dca0b9-1dfe-3f1e-b03b-60d8461bbf2e | -7.11294 | -42.64214 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0ce178a1-ca5c-3c25-8046-43a0125ea910 | -9.94756 | -44.0845 | 2024-10-07 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71b73c16-8e32-3dfe-abf0-318a7bc7173d | -9.9471 | -44.088 | 2024-10-07 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c092c257-07b9-3e92-a2bf-9efb16e7b8cc | -4.28942 | -43.73284 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0e7309b-2567-33cb-8d42-aa9192867be6 | -4.28436 | -43.73197 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f663b310-5b88-34a6-ae4e-b86d99e940f5 | -4.28392 | -43.735 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d6f7b34-4190-31d2-80bb-f41911e2eaaf | -4.28348 | -43.73802 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14f9d3f2-eed6-3e6b-9b3d-3f39ae74b9fb | -4.28305 | -43.74096 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f81c552-ca6e-3361-a018-195b23097d29 | -4.28262 | -43.7439 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b07ec628-cdd5-3cc9-a5a2-a187ad5fe9cb | -4.28219 | -43.74681 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f1bc439-4c3f-3600-8ede-d0b6260b79f8 | -4.27932 | -43.73102 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e05b3aed-a984-33d0-81bd-ead07b38659a | -4.27887 | -43.73409 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e43ff88-847f-3ed1-a0e9-14235b6c8bef | -4.27842 | -43.73717 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 00da1939-390d-3ece-9b89-b3769a31f32c | -4.27799 | -43.74015 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1394049a-4776-388b-897a-2200cf2ad15e | -4.27756 | -43.74311 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 457bdea1-a4db-39f5-90ff-53bbd295636d | -4.27713 | -43.74605 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a1826234-abee-3f23-a570-97abb8ed8a23 | -4.2767 | -43.74893 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1c6bd688-e8ac-34ee-93ac-5efbdacc18a7 | -4.27628 | -43.75181 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17982445-1fce-3287-84d9-1a891dc20ec4 | -4.27428 | -43.73007 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2683642-b70f-3db1-8e91-d2a03b4ed7ed | -4.27382 | -43.73318 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93f40ef1-9afa-3130-89d5-b74a6975a187 | -4.27337 | -43.73628 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e61bf075-c89a-3345-a8a7-92692400073b | -4.27293 | -43.7393 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a97b94b0-328c-3b76-8931-4458e128c366 | -4.2725 | -43.74227 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| db09c976-4542-34f8-a139-78df4145c93c | -4.27207 | -43.74523 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 33213247-c30f-3e8c-9136-bdf2c8d6bbcb | -4.27164 | -43.74816 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d7afc4a8-7263-39bd-a6f7-2d5ec07fc23c | -4.27122 | -43.75107 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dfd84315-235f-3238-89ef-f0ebd10e4ac8 | -4.26922 | -43.72918 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1ed715b-d4bf-3ea5-a69e-50a7e96d9b67 | -4.26878 | -43.73224 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 792c799f-8130-3f66-adea-37803895c75c | -4.26789 | -43.73839 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cecff706-8a8c-3056-8bef-c9378cdce392 | -4.26745 | -43.74138 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0d69f602-b572-3553-ba6b-352b025c2c66 | -4.26702 | -43.74437 | 2024-10-07 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README79.md)
