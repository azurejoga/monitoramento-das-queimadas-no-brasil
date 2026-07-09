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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fb006ea-9c1f-3c0d-8661-2d0858226758 | -13.28061 | -54.4166 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4295a233-54dc-3540-b8a5-682e112ebf54 | -13.28118 | -54.41235 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0aa4626-c7ad-3ce3-b7d2-23b70a4512ac | -13.29863 | -54.34891 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 264aad23-82cf-3963-9eb4-b8c98136a5fa | -14.14981 | -52.88602 | 2026-07-09 05:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1f62669b-0ed6-384f-b328-daa0fd164e2b | -13.35305 | -54.37608 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef5fb2be-b888-3330-878a-366aafad1d9b | -14.14489 | -52.88525 | 2026-07-09 05:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4133a04c-12dc-3616-87fb-ad6bd6c1136f | -13.35361 | -54.3718 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0866aa1c-c925-389a-8acd-868e1e024c66 | -13.28996 | -54.41361 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65ccd452-8491-3520-935b-951a29984312 | -12.84771 | -58.31052 | 2026-07-09 05:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3bb9581-38b2-39e5-baca-13c5d1be8a2d | -13.30304 | -54.34959 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d34ec0e-828e-3641-8da6-9ac7cc7916e3 | -13.29099 | -54.33879 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fd91532-b799-394d-bbbd-2fc884bd0e21 | -13.3492 | -54.3712 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f6eb4f0-fbc7-367f-9973-724bddc89adf | -14.44086 | -48.76166 | 2026-07-09 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d22e7984-7b97-3c02-93e4-80cd02752aa4 | -12.8512 | -58.31105 | 2026-07-09 05:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c52a26b1-abe3-318c-b39d-59bfeb6132db | -13.2954 | -54.33947 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d169b7bd-6774-3bdf-817f-a21ca79933f3 | -13.27621 | -54.41601 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 170c6eb5-4fff-3dc6-a6bf-06d2331f4b00 | -18.02194 | -54.3602 | 2026-07-09 05:29:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e359234c-9967-35d8-bf5d-3aa9d54fe868 | -13.34864 | -54.37547 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c21aab29-401c-3c68-8b0b-a2dd55ed8b41 | -14.44145 | -48.75634 | 2026-07-09 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c68081a-3cbe-3a95-89c7-4268552d7d28 | -18.02257 | -54.35504 | 2026-07-09 05:29:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0e15d98-4b6b-3ae1-88e6-9a9283e01124 | -13.30245 | -54.35397 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe87b2d5-ef69-3bbe-9333-368bbdd31ab5 | -18.02386 | -54.35661 | 2026-07-09 05:29:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb502c02-39c8-3357-b0bd-1b19c1a722a8 | -13.29217 | -54.32992 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23386271-d8c4-33ad-84a7-f5ff04f40d7d | -13.35417 | -54.36749 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb696570-6b54-398b-88fa-0b2b3bda5b1e | -13.3613 | -54.38165 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 651e8417-8cc3-3a33-949f-436b85ffa5fa | -13.34423 | -54.37487 | 2026-07-09 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a44f709-44e0-36cb-941b-b134d1c019f6 | -14.14909 | -52.89169 | 2026-07-09 05:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2429d9e7-5985-309c-82bb-c94e15ba1a29 | -21.80092 | -56.26671 | 2026-07-09 05:31:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 118e47ff-617a-3eb9-beb0-ff77903a0f98 | -21.81218 | -52.71786 | 2026-07-09 05:31:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18105ea1-83e9-343e-aeb8-3f2e6a3b1b98 | -21.7955 | -56.27507 | 2026-07-09 05:31:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e9c2b9a-a412-3891-bb9d-e997eb2a065c | -21.77592 | -56.29061 | 2026-07-09 05:31:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a060a2b-0e60-338d-8127-0ba6c95c1746 | -21.46016 | -54.48553 | 2026-07-09 05:31:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 85fc9d56-40e2-38fc-ad28-651a31d8907e | -21.77155 | -56.29007 | 2026-07-09 05:31:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f1a488d-05c4-34d2-bfad-88ed9a7f4499 | -21.80667 | -52.71727 | 2026-07-09 05:31:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89e12d0c-6d10-3eee-b350-aa132bedef4d | -22.92278 | -49.20598 | 2026-07-09 05:31:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ffbc53d-252b-397c-b39e-a07013d62862 | -23.2198 | -55.48327 | 2026-07-09 05:31:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 49a5274a-472c-35c2-84c8-d2ab1d83b334 | -21.46566 | -54.48047 | 2026-07-09 05:31:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 622484e5-538f-3cd9-8089-bc7e9837126e | -21.79601 | -56.27069 | 2026-07-09 05:31:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d81a9878-89de-3846-a88c-d23641a8fd25 | -21.80641 | -52.71883 | 2026-07-09 05:31:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 773751b7-4d9f-305e-a723-01559030e419 | -23.94355 | -54.28356 | 2026-07-09 05:31:00 | NPP-375D | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b58e4178-622a-31e9-aff8-d3330adbde5a | -23.21686 | -55.48525 | 2026-07-09 05:31:00 | NPP-375D | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0f697119-1d7f-3a8b-958b-8a37d9307bf6 | -21.46505 | -54.48618 | 2026-07-09 05:31:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 69b7d2d5-91df-35c1-a80b-1628b965236f | -21.81193 | -52.71939 | 2026-07-09 05:31:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abcef647-11da-3a7f-949c-d2fa23c8da55 | 0.87445 | -59.70554 | 2026-07-09 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 2f9deeaf-0364-3a81-87c2-fa0eb42c5b14 | -2.98544 | -54.60295 | 2026-07-09 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4af3978-61d4-3d48-810a-99b3c989f740 | -8.70298 | -54.5376 | 2026-07-09 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18ada58a-ec43-3511-a955-9007abafdf58 | -1.82403 | -54.47775 | 2026-07-09 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d9da5eb-66c3-39ca-9d38-a6e74d2bacad | -1.81783 | -54.48074 | 2026-07-09 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce79ba46-2e76-3dd6-9024-d484f65f3582 | -1.81506 | -54.47715 | 2026-07-09 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d337910-c021-3099-9f55-c13bbb2d4722 | -1.82346 | -54.48154 | 2026-07-09 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7335e6ac-c95d-3125-b5ad-8eddd34e5980 | -1.8184 | -54.47693 | 2026-07-09 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7adee4d-cf27-3504-98a5-e11e6648cbde | -6.42914 | -55.7989 | 2026-07-09 05:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27dcccb3-a7dc-372e-b419-1114c9beed99 | -8.70233 | -54.54251 | 2026-07-09 05:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 818e5c0c-9412-3dc9-bce3-f59eee1ac7e7 | -2.98806 | -54.60329 | 2026-07-09 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00aa5557-8ceb-38ec-bdde-9d2e6b10c21e | -1.82069 | -54.47799 | 2026-07-09 05:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b84c383c-86e6-3612-9452-58f0117de9fa | -6.42905 | -55.79851 | 2026-07-09 05:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7e00c48-a61b-33c7-9321-652044a8b503 | -2.98483 | -54.60689 | 2026-07-09 05:46:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38bf164c-92c3-3ee8-b541-975114395a9b | -13.34687 | -54.3716 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 265a1154-0ebd-3881-a4ba-f209e6d6db31 | -13.35885 | -54.38433 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d14f2964-0b19-3eb0-9a49-cdcbb3fb50cf | -13.3541 | -54.36669 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 760fb810-2173-305a-b9ac-c00b873d36dc | -8.60496 | -63.4584 | 2026-07-09 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d62e686e-9529-393b-8bf2-a8a98ce7eada | -13.30242 | -54.34955 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e043613e-775b-3531-ad3b-d5c13c7bb20c | -13.35348 | -54.3723 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7652cd4c-5440-3082-98e9-01ab3c269808 | -13.28805 | -54.42205 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b4d76ca-4151-3c31-bec7-761a2d07e3a4 | -11.01969 | -60.86376 | 2026-07-09 05:48:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffa617dd-4d47-31d2-8128-4c93f5aa1c0d | -13.28369 | -54.41505 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08d14455-65cf-3782-9e03-064e44fba39c | -13.29645 | -54.34272 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f5bedf64-8e55-3943-80d6-e39c9e5e884a | -13.30449 | -54.34903 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0eb4f5d-1e1a-3995-af52-424cb00f270e | -12.93258 | -56.62562 | 2026-07-09 05:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aedb4d21-18fe-3ac7-933d-e6d8f817c592 | -14.01167 | -53.92071 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12b8ae58-7e4b-3d6e-a44c-35bc4da9fa28 | -13.28964 | -54.42139 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da34f371-33f0-3b66-ab09-9525819a9f41 | -14.01102 | -53.92692 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 496bfc12-66cd-31b1-893a-8bc94074582d | -13.29027 | -54.41584 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5751173a-f631-3e1c-bd20-c4178d4071f2 | -13.28864 | -54.41648 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a51f3c5-62a5-3551-a5cc-0abedf5d7282 | -13.2979 | -54.34809 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b234e9c4-0fb8-3211-9522-799217c8f080 | -12.93023 | -56.62777 | 2026-07-09 05:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b6de5fc-6a7a-3c17-908c-492befbecbd8 | -13.30305 | -54.34365 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b913d3b-4de0-3cff-b336-75dfd859802b | -14.01717 | -53.93427 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a02ff262-d33b-39b1-9294-a329ff3d8ac4 | -13.29856 | -54.34223 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17158eae-997f-3aba-9cc7-d83b21b601cc | -12.93211 | -56.62962 | 2026-07-09 05:48:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c96305a0-6b43-35f4-bb71-a6582c757ac7 | -13.34628 | -54.37706 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5dae417-4395-3b05-9120-6270ff7dd201 | -13.28207 | -54.41563 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92431d9d-9587-3d16-a69d-f2bd5c8456f5 | -9.02021 | -63.53437 | 2026-07-09 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f949914-0d3c-362b-8d06-1717bfbb73fd | -13.35288 | -54.3778 | 2026-07-09 05:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b20563a-06b5-3629-adf0-4181ad5d41c3 | -21.77707 | -56.29052 | 2026-07-09 05:50:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86f20c28-4f78-3a3b-8a10-3cdd4200d638 | -21.77061 | -56.29008 | 2026-07-09 05:50:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf9b1b79-c308-393e-b016-f5449a89450b | -7.7056 | -45.171 | 2026-07-09 06:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 9426e68e-166e-36a5-a33b-49889eb26e28 | -7.7056 | -45.171 | 2026-07-09 06:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| cbab1fc6-80ec-3071-9fb6-36fa992953f7 | -7.7056 | -45.171 | 2026-07-09 07:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 333af643-e7d0-3bae-9647-9771cca3953e | -7.7056 | -45.171 | 2026-07-09 07:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 6f79c297-160e-3296-8caa-c26a90b01fed | -7.7056 | -45.171 | 2026-07-09 07:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| beaf5b19-e819-33d0-9e83-8cd7b4580fa1 | -7.7056 | -45.171 | 2026-07-09 07:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 214.3 |
| afc1daa3-afc0-36e5-961b-eada95fb80ef | -7.7245 | -45.1692 | 2026-07-09 07:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| cc69f0de-5884-3548-9cc1-e658c91dac2b | 0.87518 | -59.69698 | 2026-07-09 07:37:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 00a258aa-4d15-390e-a82c-b786365a1580 | 0.87656 | -59.7062 | 2026-07-09 07:37:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 47e6843b-0cc6-320a-8bc5-966dc07ec86a | -9.01611 | -63.53301 | 2026-07-09 07:39:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 886b24fd-4380-3f84-9b3b-83d21f4586ee | -13.2824 | -45.1776 | 2026-07-09 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 0170c081-5e43-3cf5-a85e-8d1cdfba7f69 | -13.2829 | -45.1543 | 2026-07-09 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 372ae55d-74c9-3e2d-8179-a68aa78295b1 | -13.2824 | -45.1776 | 2026-07-09 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| bd4294b6-ea21-3a29-80f8-e3b8f2548b93 | -13.2635 | -45.1575 | 2026-07-09 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |


[Clique aqui para ver as próximas entradas](README13.md)
