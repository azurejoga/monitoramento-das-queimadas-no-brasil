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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2713a129-2dbc-364c-8bbf-170f5a4b2a5e | -4.38902 | -41.45227 | 2024-10-10 04:17:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8c1db3b2-cfcb-3ece-aab7-ff7f4da69a4f | -4.38843 | -41.45609 | 2024-10-10 04:17:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 10649a17-d46a-3ae1-9440-a41f8dc6bc20 | -4.27963 | -41.45915 | 2024-10-10 04:17:00 | NPP-375D | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 89549765-f9ff-3f5d-bc09-13de532a2333 | -4.05314 | -40.48874 | 2024-10-10 04:17:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a342cb9f-55a4-3b31-9610-93800f0d0ed5 | -4.04683 | -40.40751 | 2024-10-10 04:17:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b8fa758a-8feb-3265-9d2b-253b2b796f88 | -4.04311 | -40.40696 | 2024-10-10 04:17:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dcd9fef7-ba59-3fcd-835c-07bf0feef9a7 | -5.20007 | -41.3086 | 2024-10-10 04:17:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7e0d6700-205b-361c-9489-cbfa117254b5 | -5.19835 | -41.2959 | 2024-10-10 04:17:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 37d9e63f-d545-3105-b89a-4ee812548df5 | -5.1971 | -41.30401 | 2024-10-10 04:17:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2909e1b4-01e5-3ab6-86c0-d56196aec3a4 | -5.19648 | -41.30807 | 2024-10-10 04:17:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f72ebddc-645a-3886-ae81-041310ad2df7 | -6.31983 | -43.11227 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a18a24f-67c8-3bc7-81ae-71c8fef96ba5 | -6.31543 | -43.22946 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56cda852-b913-32fa-86ac-a409b381cf64 | -6.31402 | -43.37862 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d725aa91-5d32-38dc-9c9e-58804e741cca | -6.31206 | -43.22894 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccb7bd13-11d8-307b-92c8-2432c4cbae77 | -6.30983 | -43.24324 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d482ee8b-8c5e-3ec3-b616-9c8bad790479 | -6.30646 | -43.24272 | 2024-10-10 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8162cc27-ab8f-396e-8336-1849b9e76a7f | -6.29328 | -43.45958 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3ccbdff-c009-35ab-a0ef-b95347b45d28 | -6.33009 | -43.76111 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6aa144e7-37fe-334b-b5fe-238b52b425a1 | -6.32954 | -43.7646 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9972b6c-869a-3353-b191-9ed070f6392b | -6.32742 | -43.80007 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 796f329c-08b0-3dc7-a036-04ebe631e383 | -6.32675 | -43.76059 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a49fe2fe-95bd-3729-b6f8-70e13d3b7275 | -6.3262 | -43.76409 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd7449ef-80b5-3dde-9de6-3c50afc537bb | -6.32286 | -43.76357 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5c61036-5c7c-3d7a-a880-dda7c2c00079 | -5.81035 | -43.75569 | 2024-10-10 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d1c2ba2-7568-372e-9817-5e55ed58d7cb | -5.68637 | -43.63618 | 2024-10-10 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a1e2ac2-b1c0-3f52-ac67-c3b9d4009338 | -5.8109 | -43.75219 | 2024-10-10 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65550c36-1d77-32b8-a021-0229a95ef10f | -5.04764 | -42.96601 | 2024-10-10 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d7bf49e-4451-3077-af85-e766f6582bbf | -5.08629 | -43.79602 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c47a28f2-1c13-33a9-9e46-3ff6496ce0d6 | -5.08575 | -43.79949 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 941c7f38-0c4f-371f-b845-b6f5972fafd7 | -5.24101 | -43.4309 | 2024-10-10 04:17:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64e00d3f-2797-30b2-b225-bf96a03a6168 | -5.11333 | -43.75397 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae5a7741-1324-326f-ad72-f7b4c2be9140 | -5.11 | -43.75344 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 143fdb98-bcb5-3844-bdfb-b5bf616bee17 | -4.98375 | -43.02185 | 2024-10-10 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bb05ce5-d2d0-3feb-b89f-dee3288ae5e2 | -4.9502 | -42.98391 | 2024-10-10 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1228723f-0ed3-3a7d-9f4f-220803aab208 | -4.94964 | -42.98748 | 2024-10-10 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8c8e4c77-0436-3fef-b617-97e7f441fcc1 | -4.94908 | -42.99104 | 2024-10-10 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6bae6cc5-9e75-39fa-b640-8713305c491e | -4.94683 | -42.98338 | 2024-10-10 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 84c412b2-0715-39ff-81ad-632ddcf8d6f7 | -4.94627 | -42.98695 | 2024-10-10 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 44eb4945-7817-3742-b51f-17e1f6a64e07 | -4.94571 | -42.99051 | 2024-10-10 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a3b170b-933c-3bfa-8707-bd173ba69994 | -4.88967 | -43.0183 | 2024-10-10 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1678713b-dbb2-38ec-a83d-860b25388122 | -4.78106 | -43.06719 | 2024-10-10 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e1290a6-9dca-338e-9969-365aa69cd9c2 | -4.72109 | -42.93369 | 2024-10-10 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 58c899c4-7376-3e07-bd3b-87cb1756d370 | -4.72084 | -42.77993 | 2024-10-10 04:17:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d602964d-1df2-329c-aaa3-1a684bdf7e47 | -5.99425 | -43.46016 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ff0eed04-17ff-3abd-9ee3-921f8fae8ea0 | -5.99992 | -43.48995 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3ad7bd96-0c50-3ffc-801a-a073a2f489d6 | -5.99711 | -43.48592 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 789bd081-8004-34e4-b50d-1685a0a46440 | -5.99657 | -43.48945 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e55a2729-9f39-3730-9526-08916a7b5397 | -5.99602 | -43.49296 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ffebc65e-1692-363d-b526-ef2b095d2536 | -5.99486 | -43.47836 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b6adc08-eccb-3ab4-afbe-4cbab371bcc9 | -5.99431 | -43.48188 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e8611ee0-7982-3cc5-9882-27c45fb4a791 | -5.99376 | -43.48541 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10c34e22-efb4-339a-8227-fed64824c0f8 | -5.99151 | -43.47783 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ac69ed9e-e2f6-363d-91ba-781c40dcd699 | -5.99096 | -43.48137 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00fadf83-be8a-3bcb-b9b1-0da1e1f782c8 | -5.99041 | -43.48489 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc447f48-69ce-37cb-a174-e1d21cdd02cb | -5.98761 | -43.48084 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c1275fa8-0cf6-3454-80d0-fc6a5ddf0510 | -5.98706 | -43.48436 | 2024-10-10 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 271f10d0-a1ee-3e6c-b6e3-1ab7fccb8dfb | -5.96574 | -43.79738 | 2024-10-10 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fc8a2c3-ede5-3b72-b8f7-8abd2f7b3a90 | -5.96465 | -43.80436 | 2024-10-10 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d858906-d4d4-32a1-87c6-783680a73697 | -6.64224 | -43.79883 | 2024-10-10 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 549ad63f-17c1-3bfe-8029-8bc17104ea70 | -6.61927 | -43.16094 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 948b8d0d-7ca5-3d7e-ad13-c83c4e87b506 | -6.61644 | -43.1568 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5713291b-4d2e-3554-bbc3-65aac8f57f52 | -6.61589 | -43.16042 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b82b34d2-4c8e-3093-b7b5-bfd5a4cda4ec | -6.52851 | -43.22861 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8549e702-be8c-313e-a9e9-a6db2d81492b | -6.52457 | -43.23167 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa7de88f-1052-3f5d-b9ec-c974b912b6ad | -6.48988 | -43.34381 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9ae7e67-fa9f-33b9-8feb-0218b4fb3e29 | -6.48375 | -43.36106 | 2024-10-10 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 458c9cf1-e33d-307a-a3dd-7aeea065fcf8 | -6.57555 | -43.83163 | 2024-10-10 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c672f42-cd6d-32ff-a215-15eddb599368 | -6.52667 | -43.64717 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26c65906-96b1-3c1d-9c03-e33f8aa753e6 | -6.64169 | -43.80235 | 2024-10-10 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63594c4c-02ad-3103-86dd-7b43fff6c675 | -6.63835 | -43.80184 | 2024-10-10 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad7b9f70-8bef-3182-92fc-a31d9a2c3ee4 | -6.45345 | -38.84793 | 2024-10-10 04:17:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 84925a1b-6f58-3465-830d-eb9b0578dfa7 | -6.45333 | -38.84678 | 2024-10-10 04:17:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1b23f464-7a2e-399f-8487-d6cd80f1a41b | -6.44909 | -38.84622 | 2024-10-10 04:17:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6af72ba6-7b6f-3d20-b7ea-1793ebe0f4d8 | -5.92128 | -39.21533 | 2024-10-10 04:17:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7b4a4100-a7d4-36b0-b15d-86cad03d5019 | -5.91719 | -39.21469 | 2024-10-10 04:17:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c1839be8-fa52-37c8-958b-e1d67cfc7de3 | -5.91666 | -39.21829 | 2024-10-10 04:17:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 234a82a5-55ef-34ab-b5e1-66d59ccd46e7 | -3.96291 | -41.4815 | 2024-10-10 04:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e32c4a75-0fab-3fd9-b40e-f962395016c1 | -3.96231 | -41.48539 | 2024-10-10 04:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a3a9a30d-ab94-3fcd-9179-900ea5085701 | -3.9567 | -40.72372 | 2024-10-10 04:17:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| db21825d-04c1-3891-96e0-b1534251db63 | -3.89014 | -41.03818 | 2024-10-10 04:17:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6976a00e-cf35-3917-9252-93e8084986c6 | -5.39597 | -41.2476 | 2024-10-10 04:17:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f3dc5bee-8280-30da-9f10-4b983ca0287f | -5.39236 | -41.24705 | 2024-10-10 04:17:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 27b78a3d-c55d-3d12-a642-3ad2c1f60033 | -6.37195 | -40.47667 | 2024-10-10 04:17:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5da600c7-45ee-3cda-a092-3358fd704f70 | -6.30356 | -41.76882 | 2024-10-10 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ad2d404c-9cf5-3d6d-a05e-dab9cc1b044f | -6.30063 | -41.7642 | 2024-10-10 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e38d8017-f62c-3b38-bbd4-9633ede6e352 | -6.30002 | -41.76823 | 2024-10-10 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e5c29771-d9cf-3a39-9e76-43f2bbfc933a | -6.29647 | -41.76765 | 2024-10-10 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e5716cfe-b942-3f2f-b2df-08c515af2ebe | -5.19601 | -41.28724 | 2024-10-10 04:17:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f23472b2-f6a7-3a33-8906-0fb50c751a5b | -5.19539 | -41.29129 | 2024-10-10 04:17:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89207982-2b58-3d6b-804f-a88e36eaf46e | -5.19289 | -41.30751 | 2024-10-10 04:17:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 00596288-05b1-38f9-b2e3-415a132e518e | -5.18993 | -41.30289 | 2024-10-10 04:17:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5098bc42-cd1e-3877-9c17-d4315882a61a | -6.48305 | -41.9614 | 2024-10-10 04:17:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2accaaee-47f1-37f0-8593-71d8b1a9fa0d | -6.48072 | -41.95298 | 2024-10-10 04:17:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a551c5c4-0a56-3fe2-957f-2b35743d177b | -6.48012 | -41.95691 | 2024-10-10 04:17:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bb9b3a13-65b3-3252-ba99-773fc5bffb74 | -6.47953 | -41.96083 | 2024-10-10 04:17:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8486d426-c533-317d-818f-03d8f21a663b | -6.42132 | -42.01179 | 2024-10-10 04:17:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e0d53c42-80b1-3051-b30b-8877bbca0ee8 | -7.09701 | -41.4468 | 2024-10-10 04:17:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| fe4b11b2-dda8-31e7-9c91-044837fc793f | -5.04635 | -42.48024 | 2024-10-10 04:17:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 13e59d90-c917-3be3-b228-6c157d03c221 | -4.71942 | -42.94438 | 2024-10-10 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfe6ea6b-419e-326b-96bf-0c7311456239 | -4.71772 | -42.93317 | 2024-10-10 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README57.md)
