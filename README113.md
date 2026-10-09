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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c840c9d6-be8f-3c57-8040-075158e60a0b | -9.42878 | -45.81539 | 2026-10-09 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf149bf1-b483-3d0b-9ecb-ad119024f6c3 | -7.87445 | -44.14447 | 2026-10-09 04:27:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8b16020-34c8-39df-9a7b-87ac63a6c584 | -13.87738 | -43.80354 | 2026-10-09 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3d8b8217-2417-36a3-afa7-7bb702193951 | -7.96409 | -46.88467 | 2026-10-09 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5c031c8-5edb-3633-a2a0-e1ec16fcf027 | -8.97337 | -45.16703 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 36e8f080-2dc0-3d0b-a40a-c4c1e50461ae | -10.86644 | -45.54113 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5715ad27-227e-33ca-bd63-26fee836614e | -8.74208 | -45.14341 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c4cc5873-0bae-3eb8-9d45-1679160b10ad | -13.1225 | -46.32413 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a77533f6-6c6c-3bb9-b976-3e5dd51f05bb | -13.55795 | -49.15683 | 2026-10-09 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f937124-fc72-353e-9913-5bb6d8808ac1 | -8.51892 | -46.90504 | 2026-10-09 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e255a09d-3ba9-3386-88a8-d27d3c2068a4 | -8.49275 | -54.63014 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bfae0467-a919-317e-bbd4-1165415781c1 | -11.22148 | -45.32213 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 17766cbf-2cbc-39a3-8576-13eeb08af36b | -11.46285 | -43.38745 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| acf7a6dd-90f0-308c-b7ea-d4dd8d80682c | -7.17829 | -52.61291 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f96e4fdc-3371-3a35-accd-8b439a25b4f6 | -6.8489 | -59.39692 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| feb03219-1fa8-3abe-9f5f-b2b633a2f93f | -6.04025 | -53.49178 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8376071c-26db-3d1f-a786-b97ca8fe67ba | -7.50937 | -47.33408 | 2026-10-09 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 132f45ec-d465-3282-9d39-fa81b418c625 | -10.25777 | -44.64248 | 2026-10-09 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ef5916b-31fa-397a-9077-ba96aa5e4886 | -9.88212 | -50.48926 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 802fad36-23c3-39b6-8615-f4e9a383fc62 | -11.41037 | -46.6826 | 2026-10-09 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74dc630d-a349-3179-b9f7-6ea8968e4179 | -11.21299 | -44.86417 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ab605dc-36bb-3913-ba2b-11b375bc7656 | -9.14601 | -45.81584 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0efa177-cc14-3b6d-b8f6-416877d6e00b | -6.14007 | -53.50993 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faf78148-99c5-337a-8dba-8c92d8baa761 | -7.30148 | -46.15916 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a0680ce-93cf-3ce3-b42c-b4098af68312 | -6.73073 | -48.12017 | 2026-10-09 04:27:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 32bf05b7-991d-3519-a511-1bd8ee6b5f2a | -11.78116 | -45.54206 | 2026-10-09 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03d67bd0-49b7-33e7-83a7-5e9865506dc2 | -11.06345 | -44.02464 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e85807f9-2609-3114-8d7f-7ad8e8cc0cf0 | -11.21358 | -44.86016 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 582c8a42-4ee1-3cec-855e-abf8fc74cb56 | -11.7621 | -58.28677 | 2026-10-09 04:27:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90754be4-1d86-3971-9df3-6cc6c8e689c0 | -7.38301 | -46.22578 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87990f66-fa2c-3f17-a6d6-68da45a482a1 | -14.0789 | -43.78067 | 2026-10-09 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 293f2039-e8c8-3fc5-8f8b-377559ea154c | -13.63687 | -44.42439 | 2026-10-09 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4947d594-8dfe-35b7-97e9-22e3ee627a2d | -10.68308 | -44.33073 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03013541-5f8b-3c1d-8ae3-00d949c5e0c6 | -11.91125 | -46.56359 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 529dce04-91ee-3d2a-ab6f-ffda64039f51 | -13.75624 | -43.62635 | 2026-10-09 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21ef6164-e664-3d78-82bc-25fedabff5b4 | -11.28201 | -45.20105 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad8f8004-f73e-3ccf-a61c-24dc38ac4fbb | -14.17449 | -48.66234 | 2026-10-09 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34f0b930-2446-34d0-806a-d5076f828857 | -9.29976 | -47.46041 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bd96b95d-dd42-358c-a1b0-ce72728019ea | -8.96931 | -45.12464 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b347497c-02be-3a4a-b74f-be9bca3a8c5b | -9.21457 | -57.72847 | 2026-10-09 04:27:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96a0d236-9a3c-3061-b520-6e2cc6f0a271 | -12.2226 | -57.08448 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 995fced0-1116-30df-9cea-4456245c5fe4 | -10.40918 | -47.28552 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af6bd27a-bbb4-37b2-b8e1-e15d398c2649 | -11.09349 | -47.63195 | 2026-10-09 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cec2d2f3-b7d9-37c7-b1ed-8702a65386df | -7.79689 | -44.57754 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c4dd7c5-9c39-3144-b8f6-2540cbc3cf25 | -9.02824 | -46.86942 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 250f963b-f268-39c3-b82a-e8f584a47016 | -10.29809 | -46.59835 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ed208f7-2f2a-3cac-bec8-d6a6b3cec03d | -8.73137 | -45.16827 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fddfeaf1-9c71-3424-b41b-3a6d82cd178f | -10.89448 | -48.39833 | 2026-10-09 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39b34cb2-6358-35f5-a696-6e1ed1b7708d | -9.12989 | -45.83182 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5db7c182-8c59-3f80-8a84-81afe75ac270 | -13.13268 | -46.32558 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49d90228-0439-31d1-bee9-6e2ec7bc41b9 | -13.18411 | -54.36377 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6e6dfea-cbad-3744-a6cf-5f673249e419 | -12.17766 | -57.09583 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d06693f7-d2ea-38cb-840f-75983451f408 | -11.0548 | -44.05895 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b82f951-7739-33ee-a3b8-cc078fc77eb1 | -6.38129 | -56.22776 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82279895-66e3-3a34-818e-28ebcaaa0e40 | -8.98682 | -45.90455 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6f9bcf6e-2162-32f4-bd49-b3b35f96a7c9 | -11.76144 | -46.7886 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a1a12b1-7365-3878-9aa6-8f80bcf0da22 | -9.26117 | -60.88062 | 2026-10-09 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 618706f1-a612-316f-9a41-ef63b9f3cbf3 | -8.9162 | -45.2229 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abcd8185-1a42-333b-8687-fd3fc1a6501d | -6.11613 | -55.70419 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66db154f-a3ce-37e1-a154-059b15cfeae9 | -13.1727 | -54.35286 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82b38ae8-2b51-3324-b20a-b5214108801d | -11.24712 | -46.30233 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea8e44a5-de07-363e-9cb3-0db89454ffb7 | -11.65255 | -43.68959 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a351d26d-5c50-32c4-9000-b3dd3fe91743 | -7.58449 | -45.64798 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e9028cb-32fa-3e90-af49-203331f34b3f | -9.92037 | -44.79242 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 517e1713-1bb2-397d-9318-7520202af886 | -11.05301 | -44.04533 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ed7c9390-7dac-378d-8024-49c75aa0f18d | -11.99459 | -43.48209 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 54c0c59b-b531-3386-ac6f-d517ee823030 | -7.6145 | -46.98829 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e6a11c5-c286-35e1-adf7-2a6598b275f0 | -12.1005 | -57.15414 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a1eb828-1c22-3ab5-924d-ad4624a6e00d | -10.32027 | -46.609 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 476bd490-9b61-30c2-a21d-c72698620bab | -8.22287 | -46.4039 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8aad85e5-ad24-3088-b133-178e0d15afdf | -8.59816 | -49.52591 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 577efead-98c0-3c66-94be-bca5c46f7af5 | -7.3887 | -44.46666 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac55830e-d5fd-3262-ae73-03770f26fc1a | -9.08639 | -45.1149 | 2026-10-09 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e116dd8a-41f1-3cd5-89d6-144a6a8850af | -6.01178 | -53.49178 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e455d9f8-41d4-3a56-8ec7-21147402623e | -12.21489 | -57.13073 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c68a3cd8-9860-3353-801d-fe9dbbb4299c | -11.72143 | -43.6379 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0e5573b4-0797-3b6b-9a0f-c5a46d3ca9d1 | -11.3088 | -44.8282 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a94a1acc-0ea2-3293-a258-dca833400469 | -12.24302 | -57.092 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e034f7c0-5bb6-3ae3-9a7c-f473c6ec766e | -9.89888 | -44.79313 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 78931d79-a1c2-350e-ad96-7afe319a13b1 | -6.07264 | -53.60439 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a7af517-38f9-387c-a595-6984a1cc0e36 | -13.15015 | -54.34545 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6dc05d84-2189-3081-bea0-a07cff8bd516 | -13.16031 | -54.33863 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6868de1d-15d3-31c6-a928-a724aaa31925 | -10.10682 | -48.7435 | 2026-10-09 04:27:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6eed678-db85-3ebc-a62a-e3a218f80d78 | -11.67503 | -46.7753 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6897f1da-445f-3437-94a4-563ead66c57b | -12.20755 | -57.13337 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a5cf946-943d-3573-810a-e2b858759094 | -11.77219 | -44.95098 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 621af097-27a6-31b8-9349-7211e27e7992 | -8.99272 | -42.34144 | 2026-10-09 04:27:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9811f894-7b68-3cd2-a0ee-a54431b3a252 | -11.60731 | -43.71165 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f3e9b499-a80d-38f8-b5d4-67c88fe5177a | -9.13432 | -45.82519 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4b17d4d-7c3a-3371-b39f-c8651238e13f | -13.50584 | -44.37062 | 2026-10-09 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| af2264dc-fd02-327e-8001-b2c73b11e067 | -5.96436 | -55.36923 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c5c0018-8d22-355a-b737-615a962aa526 | -8.65259 | -54.53296 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 705c7518-3391-3753-8201-eecfc3ce4917 | -7.85461 | -44.96152 | 2026-10-09 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c7ec179-1061-3ba7-aa52-6a4103ccdbc5 | -13.02773 | -46.81849 | 2026-10-09 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd0ded3c-5bd8-313b-acf3-d434e66aa1dd | -11.20314 | -49.41658 | 2026-10-09 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e04d5c7-a8aa-3ec9-914d-257f6ad460f5 | -11.79466 | -46.77176 | 2026-10-09 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 138d2531-049c-37b2-8af4-749d53eef4e4 | -6.17513 | -52.86488 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d12477e-f834-3908-82dc-8b07e6dce08b | -8.40962 | -49.54456 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5b626a5-e719-333b-b5f7-991d99e494dc | -7.48872 | -42.82507 | 2026-10-09 04:27:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 01cae341-f305-3029-8135-6e791e3e38b5 | -6.48906 | -55.30798 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README114.md)
