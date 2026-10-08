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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f57f38e2-7ea5-3823-b81a-2304bacd4079 | -9.9067 | -44.79704 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd777271-95dc-3d39-ad9b-11e0f230c810 | -14.91752 | -48.10766 | 2026-10-08 03:45:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30c0531e-efa4-344f-a1d8-f60cbefb0e1a | -11.73863 | -43.64577 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 107cfbee-7b16-3431-a846-365f6271d44e | -16.89426 | -40.89888 | 2026-10-08 03:45:00 | NPP-375D | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 861e7862-10b7-3d14-a061-3b6c254d30a8 | -14.5375 | -40.32106 | 2026-10-08 03:45:00 | NPP-375D | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 29a8e53c-0920-30da-858c-b237b56b99a2 | -11.73945 | -43.6417 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e062e703-91b8-320e-a07e-55f91122fc14 | -9.82831 | -44.78483 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67b9b723-2eab-3b0e-8ba4-27e0844d9d64 | -9.91816 | -46.79548 | 2026-10-08 03:45:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3d23fa6-205f-3691-b433-08ba7eb62e9e | -15.55351 | -42.97513 | 2026-10-08 03:45:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae4e25be-bd31-308c-811e-8d9d3d464b68 | -9.89788 | -44.81239 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 621e68e9-255c-3d77-8c23-db7e99f9eb7d | -11.64617 | -43.69221 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e48d5b9f-7a4d-3b0a-b70b-07f5b0b4f564 | -10.44416 | -46.84976 | 2026-10-08 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1c5101b7-c880-3507-977a-5b41a2346a17 | -11.24312 | -46.24883 | 2026-10-08 03:45:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8f29770b-1b0e-3c06-94c9-feba6cc63c94 | -15.42027 | -43.7036 | 2026-10-08 03:45:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 595ad3b1-9b4a-3786-b50d-070c92c2e78e | -9.9095 | -46.80131 | 2026-10-08 03:45:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f174d210-7f86-37f7-aba6-cc885f5b8d53 | -9.91301 | -44.79862 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f0808558-edbe-3694-a0bf-f43a11b19fab | -15.44978 | -42.02693 | 2026-10-08 03:45:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e19a50cb-6feb-303d-ad67-acb40e4a1bfd | -11.84965 | -43.53619 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e971c752-3571-3637-baf7-7d1f36a840fa | -11.75472 | -44.93695 | 2026-10-08 03:45:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c49a982-2f8b-3747-804c-0b67e6f0256c | -9.81765 | -44.77889 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06fb76d5-56fe-36f0-a17c-3a63d38567cd | -14.92439 | -48.09448 | 2026-10-08 03:45:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92b3c407-1aaf-38fd-9b2a-16273c3fe026 | -10.29965 | -46.62152 | 2026-10-08 03:45:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1dd9fe44-25f9-3a2e-a9bd-3acf667ce40a | -11.63306 | -43.69796 | 2026-10-08 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9fbb2926-376b-3f7f-95d7-d4168533732f | -9.36998 | -45.94039 | 2026-10-08 03:45:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9b4b49f-8ee6-3e67-b3b2-b5187a6aa110 | -13.15725 | -43.28383 | 2026-10-08 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 03a6c573-0547-34c7-b2e8-33d05006197f | -9.89819 | -44.80679 | 2026-10-08 03:45:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 247e7357-651f-305e-af65-727e2a4d2545 | -16.01457 | -43.60538 | 2026-10-08 03:45:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8b38883-157d-3a54-bb20-72661c45b96a | -17.116 | -41.34124 | 2026-10-08 03:45:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f8375b3a-7ef7-3c59-bd8d-71ce7659a966 | -20.31602 | -41.35299 | 2026-10-08 03:47:00 | NPP-375D | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 637341d1-4440-33d8-9d99-83d738502ee9 | -18.98494 | -46.57903 | 2026-10-08 03:47:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da6696ea-bd62-3e03-ae8f-cb035a25caeb | -19.99407 | -49.0907 | 2026-10-08 03:47:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a8c9a4f-cfc7-3a3d-a15e-7b51455c309c | -19.31191 | -40.90163 | 2026-10-08 03:47:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8c6962c1-cc65-3d26-8e43-4abb81c42888 | -17.71199 | -42.0293 | 2026-10-08 03:47:00 | NPP-375D | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5e9c68de-35ef-31ec-b020-850600cb08ec | -18.38862 | -40.31874 | 2026-10-08 03:47:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b98e877b-bd36-3045-b052-c74f75852165 | -18.986 | -46.57443 | 2026-10-08 03:47:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79ca34e6-a44b-32d4-a5bd-3f2fadef845c | -18.98442 | -46.57827 | 2026-10-08 03:47:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fe3bc7a-ba61-3856-8c2a-7bed09a1cb8f | -17.43002 | -43.64698 | 2026-10-08 03:47:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10573664-c232-34a4-abe8-3bb5e4a337c9 | -18.38451 | -40.31787 | 2026-10-08 03:47:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9c32019e-2018-36c6-a3f1-b1eea127ef38 | -18.37231 | -41.96044 | 2026-10-08 03:47:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b76ad96b-6e07-394f-8ea1-3fc6910ce0e6 | -18.37696 | -41.96099 | 2026-10-08 03:47:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d330ff4e-10c2-3862-bc83-b9a6f89622f0 | -18.62457 | -41.28099 | 2026-10-08 03:47:00 | NPP-375D | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 18627a88-fe63-3cdd-a069-8c23b8d181b0 | -17.97695 | -41.45004 | 2026-10-08 03:47:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0631f9f3-c34a-348d-8122-75ced6eaae28 | -20.31369 | -41.35507 | 2026-10-08 03:47:00 | NPP-375D | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 83fe62a8-242b-394c-a876-1b164c2d648f | -18.72193 | -39.89953 | 2026-10-08 03:47:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c353e9a9-eae2-3c06-8207-dc0be72afb1a | -20.31181 | -41.3519 | 2026-10-08 03:47:00 | NPP-375D | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7803cea1-0455-3a59-ae60-13ac1375e68a | -18.25977 | -42.17163 | 2026-10-08 03:47:00 | NPP-375D | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3f7e391b-8f5c-3e4b-9888-5df8b48d4860 | -18.98545 | -46.57368 | 2026-10-08 03:47:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b6180f2-e040-333f-bcc1-d1953bfeb703 | -17.76028 | -42.42644 | 2026-10-08 03:47:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8835075b-bd7c-388f-968a-283179d835f8 | -18.10179 | -42.54536 | 2026-10-08 03:47:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c36270bd-d9aa-31c6-8e56-0f407e55cf73 | -18.10654 | -42.54643 | 2026-10-08 03:47:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c236874f-63d8-3926-a8a7-715dfcc3dff5 | -17.76505 | -42.42739 | 2026-10-08 03:47:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 01613d76-0fc0-3633-ac7f-cc053a57c6eb | -2.4031 | -57.9041 | 2026-10-08 03:50:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| a49fc464-04e3-3fa4-87ba-cfc178548e82 | -3.1972 | -50.5592 | 2026-10-08 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 11afc8b0-9617-36d7-9dab-c35ee3d94d1a | -8.7228 | -45.1812 | 2026-10-08 03:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 43cfc4f0-97b3-392b-b8f6-0c652e78c0e7 | -3.11 | -54.1862 | 2026-10-08 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 683a3c7a-f2c6-3d3e-a2cd-ee1a8b4c50dc | -8.742 | -45.1563 | 2026-10-08 03:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 751394c5-eb00-338c-8b19-3c70b2ac48ed | -2.499 | -56.0675 | 2026-10-08 03:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| b57b94b6-c8e1-30c7-8be1-f7947929d463 | -3.5865 | -54.5742 | 2026-10-08 03:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| f79b3b60-ce22-3235-a233-2f6736d1ccdc | -3.1101 | -54.1661 | 2026-10-08 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 1fffeb4b-b399-3763-a33f-7719120e0ba3 | -1.5306 | -54.5558 | 2026-10-08 03:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 314d2817-9d6f-39cb-a5f6-20e7c8f15ca0 | -13.1663 | -43.2913 | 2026-10-08 03:50:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 652a4bff-b9e7-3fa9-bce9-54ace6d227ad | -3.9662 | -56.1316 | 2026-10-08 03:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 885a3520-bfc3-313b-86c4-32df7340a2d0 | -3.5861 | -54.6741 | 2026-10-08 03:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| a9f00342-a582-3c0b-a999-e4d2d5da2769 | -2.7797 | -54.0736 | 2026-10-08 03:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 5974b0a0-eb3d-382c-9f65-147dadfffa0c | -6.6317 | -43.73 | 2026-10-08 03:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7c5bdde8-7370-33ed-ac5d-5271ca33bb40 | -6.1429 | -47.9432 | 2026-10-08 03:50:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 2fcf976a-6564-3451-b25b-e879da21e5ff | -8.6291 | -67.0296 | 2026-10-08 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d9b1c6a9-01ec-397a-b975-9be9fa87e235 | -5.7376 | -45.1533 | 2026-10-08 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 61a1b37e-eaf1-309f-8257-99aab8518710 | -5.7189 | -45.1547 | 2026-10-08 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| b3078f1e-80a6-34d8-942f-738c63955424 | -2.4987 | -56.1659 | 2026-10-08 03:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1f2d83bb-7db2-3834-b14c-e33d6a7989c8 | -3.1114 | -53.7839 | 2026-10-08 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 44cd7328-ddba-3889-a9f2-126027a73bbc | -13.1668 | -43.2673 | 2026-10-08 03:50:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 1dc1d405-086e-3c48-b47f-6a01812e93c2 | -16.8948 | -40.8938 | 2026-10-08 03:50:00 | GOES-19 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| 7678ea16-fadb-33f0-b1a7-a505aae4ba85 | -5.6932 | -53.487 | 2026-10-08 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 8740c862-2b8e-3783-bcff-bce8c128fbd2 | -3.531 | -54.6757 | 2026-10-08 03:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 520e583b-b798-32ed-b864-0553ce7edd58 | -8.6107 | -67.0301 | 2026-10-08 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e99647f9-3696-3c5c-86e3-2e6e1b857209 | -7.0065 | -59.1223 | 2026-10-08 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 168b7582-1231-33f9-8d2f-bd49ee8c37cf | -8.6107 | -67.0116 | 2026-10-08 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 208dba4a-1853-3c51-84af-39ca69bb860e | -2.7796 | -54.0937 | 2026-10-08 03:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| b4dc1ed0-7ac4-3944-9fb2-401b128bc95d | -3.1697 | -58.6437 | 2026-10-08 03:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 16554116-294d-3e5c-bd97-76e4af948aa2 | -6.6315 | -43.7533 | 2026-10-08 03:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 58ed7b7f-23a9-33af-95a0-f22a93813222 | -6.1431 | -47.9214 | 2026-10-08 03:50:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| a8493307-ee5d-3c8d-9719-3dd60248e967 | -3.0913 | -54.287 | 2026-10-08 03:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 13d3eece-0018-3ad5-b760-8442b475d8d2 | -4.3471 | -43.8021 | 2026-10-08 03:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| d71b3f1e-8bb9-3b6f-aace-a3239285fbf3 | -8.7231 | -45.1583 | 2026-10-08 03:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| da3d7df3-8bf0-3030-8bd7-df46798445dd | -3.1697 | -58.6244 | 2026-10-08 03:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 2af7c0dd-696c-3735-8a31-557b17166b36 | -8.6107 | -67.0301 | 2026-10-08 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| f63d93b0-e2be-3279-9e62-9ec62ffa6857 | -3.0913 | -54.287 | 2026-10-08 04:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 3a597ac8-d503-311a-8f38-36270d0814d4 | -2.4987 | -56.1659 | 2026-10-08 04:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 8334618b-2069-37c5-8b05-93485fe3eaa2 | -8.742 | -45.1563 | 2026-10-08 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 01141750-7328-3a7d-ae85-cce1a42119e3 | -8.6471 | -67.1774 | 2026-10-08 04:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 257537e7-4f1b-34e1-8462-0f1b521c9260 | -6.6317 | -43.73 | 2026-10-08 04:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| af85ceec-f6f0-3f32-b8d6-44793081aeb0 | -3.1697 | -58.6437 | 2026-10-08 04:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 4228efaa-05ee-3e70-ad4d-f3d478111e5b | -1.5306 | -54.5558 | 2026-10-08 04:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 10d1b87d-a2f9-3d32-85f1-73c30926b0c5 | -3.1101 | -54.1661 | 2026-10-08 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| f2d846e9-2630-3731-a9bd-038fe0bed43b | -5.6932 | -53.487 | 2026-10-08 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 6dd80ec6-14f0-3cb7-a0b0-99e1c1c1cd85 | -8.6292 | -67.0111 | 2026-10-08 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 37f3d5b0-6224-3f39-94f2-739b5637c9e0 | -4.3471 | -43.8021 | 2026-10-08 04:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d6944f4c-e156-3a03-895b-3e90d6f34037 | -3.1972 | -50.5592 | 2026-10-08 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 87ebc002-d325-3c5a-bd58-a45a6c847a73 | -8.7228 | -45.1812 | 2026-10-08 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |


[Clique aqui para ver as próximas entradas](README61.md)
