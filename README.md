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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 669524fa-e66b-39ab-b1a5-f4db55f22627 | -6.6112 | -43.8941 | 2025-07-04 00:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8796d4ea-2c05-3439-9d5b-21360b36b1e6 | -18.4486 | -54.6674 | 2025-07-04 00:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 7b4f70b8-09c7-3f16-88a1-317523352eda | -6.2943 | -43.6891 | 2025-07-04 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 350158ac-c255-3af4-a95a-f54e6bc5bb92 | -8.4434 | -49.6209 | 2025-07-04 00:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 192c984d-35c4-3d31-b6ef-70168c005513 | -7.2405 | -43.0899 | 2025-07-04 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| b06e34aa-517a-3b91-b9ba-5a6498342f2f | -7.2219 | -43.0682 | 2025-07-04 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.7 |
| 0598f965-3739-39af-a1bc-360f812c5b77 | -17.9585 | -50.5985 | 2025-07-04 00:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 520f34fb-1571-3cfd-89bb-707b00d6c43a | -10.592 | -49.4545 | 2025-07-04 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| d537d177-58c4-367c-82f1-9a480e0bad49 | -12.4244 | -43.7037 | 2025-07-04 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 448ce7ec-7f82-39f2-a1a2-ea6836ea8638 | -6.2755 | -43.6907 | 2025-07-04 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 0860117a-0891-3d36-9d39-a90bb88f1f8a | -6.2757 | -43.6675 | 2025-07-04 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| cfd1b8e1-9a45-346e-9c0e-4efe5bdfb8be | -11.932 | -45.389 | 2025-07-04 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 2b5509cd-ca71-3b9e-81a9-4fd1da00c22f | -7.2214 | -43.1153 | 2025-07-04 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| ba0c321c-e54f-3fff-b3d1-ff625f104f51 | -6.2945 | -43.6659 | 2025-07-04 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| b774118f-8928-35da-a96a-4a07f0ad95ab | -11.9132 | -45.3688 | 2025-07-04 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 9cc2d24c-0b35-3340-bc6e-84e34ba64330 | -10.5586 | -49.1337 | 2025-07-04 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c66cd8ac-3081-3e09-b471-226e70d77dea | -11.9324 | -45.366 | 2025-07-04 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| de205a5e-e706-3afe-b8b4-e6848a7aa19a | -11.9128 | -45.3919 | 2025-07-04 00:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 7bd4aa13-8a22-381f-828b-749aa719030f | -7.2217 | -43.0917 | 2025-07-04 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 317.3 |
| 7d3b8451-a262-345f-81b7-afc78245e84b | -12.424 | -43.7274 | 2025-07-04 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 08239a6b-39ad-3328-b878-da27eff3b72f | -18.04428 | -46.0561 | 2025-07-04 00:03:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 57d3f863-9704-386d-9a78-7a75cadbce8e | -18.04486 | -46.05092 | 2025-07-04 00:03:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 9066ce4b-ce69-30fc-b3aa-34bc41ac55c8 | -6.27851 | -43.68491 | 2025-07-04 00:05:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 05776092-49e7-3214-bb35-c80a592a9827 | -10.9866 | -45.10634 | 2025-07-04 00:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| a35c475f-82bc-3201-a812-015f724e7d71 | -10.58877 | -49.46976 | 2025-07-04 00:05:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| bb083d9f-f713-3948-8621-495414f569e8 | -10.64962 | -44.49009 | 2025-07-04 00:05:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| ef946797-07d7-3e82-b338-29d136007398 | -8.44024 | -49.61766 | 2025-07-04 00:05:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d2fd132c-08d7-34a6-b399-41b90c889c56 | -7.94794 | -44.84575 | 2025-07-04 00:05:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 82572598-ab64-3b49-ac20-4d108a318b43 | -11.92228 | -45.41764 | 2025-07-04 00:05:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c33f9c97-21b1-35d2-9bbb-c810199e3820 | -6.2887 | -43.6835 | 2025-07-04 00:05:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 58b7342a-4836-3113-b8e3-31e162337337 | -6.72323 | -44.33781 | 2025-07-04 00:05:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bd2e3bfc-fb8b-34ec-bbca-ce76140a6c7e | -12.41942 | -43.7197 | 2025-07-04 00:05:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| b487147f-f3da-38e2-aa98-5377b42ccccb | -5.6616 | -46.58781 | 2025-07-04 00:05:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 04c88935-4901-337b-87df-f0e2c7d0374b | -6.61218 | -43.90387 | 2025-07-04 00:05:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6eaa8b27-8597-3cda-9a23-f9d93db4314d | -8.32618 | -46.29252 | 2025-07-04 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e3747637-c671-3683-9278-e1d0b179f31b | -3.787 | -43.24254 | 2025-07-04 00:05:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1e8dc3f2-f658-39e8-aebb-549a18a3ef32 | -11.91994 | -45.39132 | 2025-07-04 00:05:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 266.9 |
| b1304c1c-9bd8-308b-99fd-fc433ed31473 | -11.24715 | -44.89186 | 2025-07-04 00:05:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8e01ceb4-1781-39b5-b340-0f2b73b8623f | -6.27693 | -43.67321 | 2025-07-04 00:05:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| a7fa314f-f0de-3a9a-9899-da78fd484f76 | -6.49604 | -43.63819 | 2025-07-04 00:05:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7b2db92c-dbb3-3cc2-a3e9-60b274928940 | -9.00106 | -47.45132 | 2025-07-04 00:05:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 04ea8a56-10ad-3a76-9df8-d4492ca628b6 | -5.64875 | -46.5964 | 2025-07-04 00:05:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 630c6c66-f495-3c91-8a72-d4f947f639ee | -11.9327 | -45.38974 | 2025-07-04 00:05:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 1b0a3874-05fc-33fa-b0f8-b0878973c110 | -12.43256 | -43.73336 | 2025-07-04 00:05:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| f5932f4d-5ce7-30fe-9ef7-48ebf63a84a0 | -11.91748 | -45.37861 | 2025-07-04 00:05:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 783b7166-10eb-378d-bbe0-f7a9ef847cca | -7.22111 | -43.09502 | 2025-07-04 00:05:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 293.4 |
| 60ad2d0d-62a3-3b81-bfe8-dbf989e1e2c8 | -11.54475 | -47.86786 | 2025-07-04 00:05:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 9fe213f9-aaec-332f-95f6-8e6fe5fe1c15 | -10.55338 | -49.11596 | 2025-07-04 00:05:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| f801fb37-e915-3ebd-b614-2af2e9bf8d0e | -12.4213 | -43.73476 | 2025-07-04 00:05:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 93331ebf-d8f3-351c-8c2a-30e87d679b46 | -11.54872 | -47.87296 | 2025-07-04 00:05:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 05b8f6a7-9041-3d21-ad2a-941c541b1c7b | -11.91773 | -45.3722 | 2025-07-04 00:05:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| da8cc2cc-aa6a-3264-b40b-dda281983096 | -7.2325 | -43.10497 | 2025-07-04 00:05:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.3 |
| 81bba2e1-2c4b-39c1-ab7b-6984c26a0572 | -6.28805 | -43.69019 | 2025-07-04 00:05:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2befa0b4-99ce-37e6-88e4-18c83f29caf4 | -8.44459 | -49.65495 | 2025-07-04 00:05:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 52f49b06-9930-3772-8abf-7ce9d5378ffb | -7.21788 | -43.07899 | 2025-07-04 00:05:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 0772c4ec-dc90-3ad8-991c-b56808e1f8f2 | -5.28659 | -45.17396 | 2025-07-04 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8cdc63d3-552b-378a-bd40-70820269f562 | -12.432 | -43.72708 | 2025-07-04 00:05:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 162.7 |
| d5cd6102-4f79-3bc7-91f1-13dcac540d71 | -7.22258 | -43.10635 | 2025-07-04 00:05:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 3b86ee7e-136d-3949-8030-c20caec4e13e | -6.99445 | -43.54132 | 2025-07-04 00:05:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dcdde604-a1a4-37b2-9f97-675354164997 | -8.58982 | -48.20071 | 2025-07-04 00:05:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 3c31d5d7-00e1-31b4-9c62-676e7aa26730 | -6.22354 | -42.00143 | 2025-07-04 00:05:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 28a907af-bcb6-3ad3-91d8-e6306337f2b3 | -12.43021 | -43.71196 | 2025-07-04 00:05:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 31f99678-1ff7-31cc-aeee-ef4649e4b148 | -11.92222 | -45.41106 | 2025-07-04 00:05:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 0deafd6c-6d1e-3e65-a9e5-eb02ffba06fd | -5.91932 | -43.44367 | 2025-07-04 00:05:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 69b776c5-c188-3c5b-bb76-6a233d167297 | -6.28707 | -43.67156 | 2025-07-04 00:05:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b40d9959-7940-3041-b06e-f09244a9c97d | -6.2865 | -43.67819 | 2025-07-04 00:05:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 94e15b87-f245-32ed-8fdf-c9c1b1d6b9fb | -3.78842 | -43.25302 | 2025-07-04 00:05:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9e3b7c7f-ad0a-3f19-8698-a73c4beabc45 | -6.49764 | -43.65035 | 2025-07-04 00:05:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5e04d983-70b4-3719-b227-5313f3f3244a | -3.38336 | -43.12314 | 2025-07-04 00:05:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 0d2f2814-eb13-3636-a7a5-6631c0fd199b | -7.23103 | -43.09369 | 2025-07-04 00:05:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| cfde4f22-cf2c-3939-9ef0-e8326c626fdf | -8.24345 | -43.74546 | 2025-07-04 00:05:00 | TERRA_M-M | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 9372e0cb-8b67-351b-aeba-b57276f0939b | -6.61053 | -43.89125 | 2025-07-04 00:05:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 6d84209c-7c15-34bf-b016-af063e02105e | -3.38473 | -43.13329 | 2025-07-04 00:05:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 726bf241-40ba-3f5b-8766-62e34eef9a5b | -7.09114 | -49.15797 | 2025-07-04 00:05:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 6bd033d0-b646-368b-bac0-e18b5b51e769 | -5.64892 | -46.58975 | 2025-07-04 00:05:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2a5383ae-2f12-30a5-991d-4720cfabe97b | -10.55758 | -49.15398 | 2025-07-04 00:05:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| b47eb211-70d6-3789-8045-0f49459992c0 | -11.935 | -45.40954 | 2025-07-04 00:05:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| fd63ade1-dfa2-334e-91fe-6312e5d41aff | -11.93047 | -45.37061 | 2025-07-04 00:05:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 1c487223-ca85-3be9-b35b-878de5a509b5 | -5.92084 | -43.4551 | 2025-07-04 00:05:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 09cd9a46-3868-3969-a1e3-e2de7d586b79 | -11.44365 | -45.11071 | 2025-07-04 00:05:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 2c13e3cf-f364-3055-9443-4379a5b4643c | -6.74606 | -43.13872 | 2025-07-04 00:05:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 367971da-1a18-392e-9e20-8258bc2dd60e | -7.2194 | -43.09023 | 2025-07-04 00:05:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 304.9 |
| eafa4091-b8f3-31b8-97a6-a557257cb2a1 | -7.88394 | -47.13696 | 2025-07-04 00:05:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 3cd1195a-169b-3d84-9b41-19903519f04f | -5.66143 | -46.59449 | 2025-07-04 00:05:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| ce897675-543a-3327-a35c-5344147a8895 | -5.28523 | -45.16538 | 2025-07-04 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 02446e64-d14b-3380-8258-e4d9c74a6882 | -5.9239 | -43.47816 | 2025-07-04 00:05:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3654629c-e1f4-39e2-b1be-8071358e53d0 | -10.54838 | -49.12359 | 2025-07-04 00:05:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 0ba593ee-c4fc-3f0e-b68e-c4eeab6a7912 | -7.22094 | -43.10153 | 2025-07-04 00:05:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.9 |
| bf979a74-b671-3155-a80a-06f86062ffd3 | -6.22486 | -42.01109 | 2025-07-04 00:05:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 7ccd9a1b-bdc3-3042-b6ff-6a402272d301 | -7.21965 | -43.08374 | 2025-07-04 00:05:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 238.0 |
| 2ea6b082-d1f6-3319-94f9-7bc0c577e304 | -10.59152 | -49.4625 | 2025-07-04 00:05:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 0d9a92eb-cc0e-3b62-a745-ae651d952c25 | -6.60891 | -43.87878 | 2025-07-04 00:05:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| b66beeda-be4a-3d02-a669-ad3c0aef62de | -12.43066 | -43.71827 | 2025-07-04 00:05:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| c0a47550-ffd2-3817-acaf-fcf6ffec591b | -11.91985 | -45.3979 | 2025-07-04 00:05:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 187.4 |
| d7281fb0-e96a-317b-a329-22d3cc4bf5ea | -12.4244 | -43.7037 | 2025-07-04 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 2af206a5-176e-3b73-8840-f87a93a2d8a2 | -11.9324 | -45.366 | 2025-07-04 00:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| ded5513d-6d43-3ac0-8262-29d897402849 | -17.9585 | -50.5985 | 2025-07-04 00:10:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 254.3 |
| 68341e42-ff61-3a47-b457-ba69747bdb6e | -7.2219 | -43.0682 | 2025-07-04 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| c2c1ae64-ee0f-3be8-a4e9-f0318fd66c34 | -7.2217 | -43.0917 | 2025-07-04 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 340.4 |
| 80df619e-101b-3334-81a4-87af636e5b0f | -6.2757 | -43.6675 | 2025-07-04 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |


[Clique aqui para ver as próximas entradas](README2.md)
