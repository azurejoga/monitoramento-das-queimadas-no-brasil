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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19b843c7-fdef-3c09-ba89-eb9c5d6ecebe | -13.3774 | -47.0133 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cdbc08a8-c1b9-3b86-aba1-b57f83d47362 | -12.82468 | -48.08756 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55d6d146-4492-325a-8d44-97d2cba9faf1 | -11.73172 | -51.75484 | 2025-08-30 05:12:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9fff6e1-68ce-3c85-8ac3-50f9e6f159d8 | -12.93503 | -48.11728 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23da8930-5040-395f-9f3f-f4ff421f6340 | -9.76691 | -64.25945 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4a17756-3c96-3c1d-a377-ab34d84263e6 | -13.97091 | -46.32925 | 2025-08-30 05:12:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 486d9e13-7e42-3b72-ae12-0b80b5376efb | -12.84607 | -48.17464 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71a2b888-0cad-3391-a440-7b509c420f1c | -12.83232 | -48.09061 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e22bbe6a-976a-3149-85d9-c552782a74a8 | -9.72959 | -64.9082 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84fb4e35-7fcf-35de-827c-539835e1c572 | -13.36573 | -46.98284 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b765d39e-7f81-3d59-8241-00d86183e83f | -12.02436 | -57.08623 | 2025-08-30 05:12:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e258c641-e792-3c1d-8305-4602bbd9a8b8 | -14.10924 | -51.77753 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52fe4695-cafc-32bc-a14e-355931053f7a | -13.35265 | -46.86805 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 595aa441-d417-3d32-8971-384e7143399b | -9.3283 | -68.22079 | 2025-08-30 05:12:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6ad1c75-c4c2-396b-a0bc-d872fb6192c2 | -12.82547 | -48.0978 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2b632f1-ecd8-3bfb-9254-26747edc9ea9 | -12.83511 | -48.10125 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc171071-731c-30a9-ba50-cdea0f71bff7 | -12.61615 | -57.01501 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9a08d65-5c32-3aff-8562-d5fa9344ff23 | -12.64765 | -48.19909 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b317d93c-a7c4-3f0f-b2da-90abfad1e07a | -13.5153 | -46.95282 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75fc1805-7e46-3597-b890-51bbb3544901 | -12.85295 | -48.15442 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95015889-00c3-3e8c-991e-547ad6ad3dfc | -12.8975 | -48.88297 | 2025-08-30 05:12:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13e91c89-b518-374c-ba78-501f72ef59f6 | -12.9221 | -56.98073 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c304d344-9204-39f8-9c44-cff6bd7e2bef | -13.57012 | -46.92559 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 856c65f4-1a1e-31b9-9b7f-e250a84a226e | -10.42516 | -64.48374 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6c89b84-3248-3b36-a4df-f617d74d0589 | -13.36869 | -47.01374 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3022a574-aeb2-33d0-a32c-06b8b3f5704c | -13.36726 | -46.98756 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ad9a5438-147e-369c-b9b2-783d8f64db43 | -11.93938 | -57.46225 | 2025-08-30 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4f67fa6-ba3d-37a1-9a26-0c0cd0db5402 | -13.37686 | -47.01842 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 07f1f64f-6cf8-3523-95ea-c9a4ffa76697 | -13.37633 | -46.88861 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc8d5469-b064-3713-a0e4-b6dfaf032bf4 | -9.97094 | -64.95326 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acbc728c-7edb-3050-9641-68856e5bd92b | -13.46276 | -46.94115 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e762b51b-94c5-3081-8ec9-b85a7531e5a9 | -13.65015 | -46.91863 | 2025-08-30 05:12:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6f6aafe-8e55-3e8b-b299-bd3bb1c47567 | -12.92496 | -56.98503 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2efd6c29-daa1-338a-be7b-4abe8b8cb24c | -12.61577 | -57.01583 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e29dd32-8f68-39b5-962c-f8cea2b6f674 | -9.78333 | -64.24126 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdf980cc-f79d-311d-ab83-d92ba48ed09c | -10.3593 | -64.46889 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d639e28c-f1a6-30cc-b24e-098f913b6356 | -11.39793 | -63.24801 | 2025-08-30 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f4b35b4-fc1a-37ab-9249-f6c02e68d5eb | -13.3704 | -46.88361 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 442a1472-bbe2-360e-889d-ead806e9718c | -13.39171 | -47.00003 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 593e7cfd-fb4b-3f4e-9d06-2fb658c2ddf7 | -9.66348 | -65.04307 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4d5f9fa-fb2f-31c1-825a-58920772573c | -13.46825 | -46.94997 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e1cb46d-a80c-3783-a5ee-d9b8da9a9e0d | -12.86237 | -60.20442 | 2025-08-30 05:12:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| aa02dc48-fd9b-3f7a-8b10-682877260044 | -13.38431 | -47.00898 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 29c056ad-59c4-3dc2-bb6e-fcf0222c9131 | -13.38332 | -46.95784 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5130d5d0-bde0-3c8d-8f82-e3d03a5d3bb2 | -12.63149 | -57.00583 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52265bf4-3e55-3632-95b7-f582a9426b17 | -13.38273 | -46.96339 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9b6930d2-2e8a-345f-8096-c3c71f30e33d | -13.53469 | -46.95308 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d1ddaccb-c18c-3c98-8344-a1dabea50da2 | -13.36694 | -47.02921 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a42cdc2-7b34-33fc-a8d2-33e1666875eb | -13.38792 | -47.03528 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f4966b4-921f-327f-9ddc-eadbaa42ab83 | -13.38223 | -46.96808 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 116d58df-fb15-3352-bb45-5819d7ecc773 | -9.55005 | -65.69193 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 070e779f-c386-3b47-a3a7-36baa733dd38 | -13.3617 | -47.0186 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 350b866c-d048-36ed-88fc-78c39df2e979 | -12.17077 | -60.74537 | 2025-08-30 05:12:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5c60f0c-4094-3741-ab4c-25242ab5145f | -12.94448 | -48.12537 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1b8595c-f642-39e9-b532-6d01a39207df | -13.3945 | -46.95694 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71a0ee5d-85f9-3252-bd4a-bc1d4707442a | -12.93204 | -48.12954 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03478a5c-7042-3702-89f9-2a6358df43f7 | -13.39649 | -46.95559 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4f07e2f-ae8f-38e0-937d-ea1698727c5e | -13.50925 | -46.94889 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e79e921-a4f3-3da3-8c79-8e327cc57395 | -13.3802 | -46.96906 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1691b41c-eb77-3e99-ae7c-9839ce444ac9 | -14.22988 | -48.07506 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 290652bb-0103-3b09-a2b6-f3edcb5d9c5f | -13.37563 | -47.00937 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4aebeb82-9491-320a-8434-c298bddff438 | -13.52825 | -46.9528 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b159260b-10fa-36f5-8422-350e2b9cf2a3 | -12.16797 | -60.74097 | 2025-08-30 05:12:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6709a220-f4a5-35fa-bc92-778762f663e1 | -11.39069 | -63.24432 | 2025-08-30 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f155a8bb-9277-3983-8470-fcffe9a44178 | -12.92371 | -48.11174 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 986507c7-03fa-35c3-a152-527c3e810848 | -13.68317 | -46.91378 | 2025-08-30 05:12:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 286ea06a-0ae0-33ea-b9da-d80f096b40b2 | -13.39121 | -47.00473 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ad8d7a4f-2fd1-31e2-b063-8ae19e89cc5f | -13.35415 | -51.77193 | 2025-08-30 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9f2c6f0-5d49-39b2-93b8-e230cc636f4f | -13.54119 | -46.95291 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df1f741e-5632-358e-80bb-5fb31a03d573 | -13.35312 | -51.76797 | 2025-08-30 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d056f21-4065-339c-82b4-c4602fbfe8bf | -11.37486 | -54.34279 | 2025-08-30 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98f41f63-6ce9-3920-9c4f-f397fd70cb3b | -12.93993 | -48.12638 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a93d00d-8209-3f5f-8a4b-e3e2236e93a6 | -11.68619 | -63.911 | 2025-08-30 05:12:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da26a413-e3fb-3e44-8f78-a5cee46ce886 | -13.36521 | -47.00687 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 271884a6-ef88-39a1-9f9f-c128926a4a97 | -11.73627 | -51.75547 | 2025-08-30 05:12:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a468075c-ea7a-3666-bc1c-38715e05c8e9 | -12.82078 | -48.12228 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25f41df4-c9a7-3c3c-9552-285ea6a1d452 | -12.84517 | -48.18209 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb803784-9c8e-38d9-8e64-3ebbf3f40b8b | -13.35294 | -54.39003 | 2025-08-30 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71d3cd09-a87f-321c-8d96-35bd50eb5900 | -9.7812 | -64.25359 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3995d3f6-c959-32c6-b369-a267c374d396 | -12.83058 | -48.08842 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 927869a4-6800-39c1-a9a4-036915d832c9 | -13.37964 | -46.97402 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e45cd835-c1d7-393b-8489-d8308845027a | -12.83729 | -48.09906 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31b2bc8f-e129-38fb-937a-0ac6caaec3f6 | -9.78403 | -64.23717 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56dabaca-0d7e-3c00-ba18-b3c712b9bbdd | -13.36675 | -46.99234 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b097e46d-39e9-3944-a918-5f345f207bfd | -13.36897 | -51.75488 | 2025-08-30 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63fb3142-fa3d-3ead-8d9a-5f28e873a4c9 | -10.35425 | -64.47231 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 92790344-7dca-3da3-ad9f-9f2033e53650 | -13.58595 | -46.90005 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89553a0f-191e-305a-9d15-ee476b0fa33a | -12.61671 | -57.01124 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ad9f5e6-e445-3139-a096-66bc388d260b | -12.62466 | -57.00476 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 97d86608-f445-38e9-bd00-35e72d189c3b | -9.75826 | -65.08908 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 492e1cd9-8f39-302a-b730-d4313d5b9b39 | -9.89391 | -67.01795 | 2025-08-30 05:12:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a0b84bc-5a18-3f34-8ea3-1f93a0643636 | -12.95042 | -48.12578 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e1c6101-643c-374f-bbd1-bfa584baa47c | -13.3641 | -47.0173 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cb0ae3af-99ae-32af-8f6f-ad1561a08fd4 | -10.06955 | -62.89603 | 2025-08-30 05:12:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ad70708-5ce9-3c53-a452-1760e40f30b5 | -13.963 | -46.34001 | 2025-08-30 05:12:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e65c7a79-0dfa-3a5c-8882-b1067d896226 | -13.37478 | -46.97745 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04457d9f-a44b-3f81-9380-e550d3e956a4 | -9.6722 | -65.02074 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dad75ae0-2769-3349-98e4-3af9d996f81c | -13.62532 | -48.25454 | 2025-08-30 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63f20d7c-1d78-30d6-8671-08a7a130345d | -11.37799 | -54.34811 | 2025-08-30 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e6e6c3a-7f1f-306b-8ec1-a06b203ff5cb | -12.91868 | -56.98019 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README75.md)
