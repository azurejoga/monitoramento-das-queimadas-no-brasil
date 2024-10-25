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

## Dados Diários - Página 182

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2af8ea46-c42c-3606-865f-5a9a042b1099 | -0.96885 | -48.23708 | 2024-10-25 16:54:00 | NOAA-21 | COLARES | PARÁ | Brasil | 1502608 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0227367f-491a-340f-badd-7930851a5c52 | 0.03353 | -49.50195 | 2024-10-25 16:54:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 26b47f02-9f80-3097-88b8-4ed6419ca310 | 0.02714 | -49.49703 | 2024-10-25 16:54:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 9d43227b-1f8c-3def-970c-c79243cf4011 | -0.67523 | -49.5555 | 2024-10-25 16:54:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 677f56fb-e647-37e3-ad98-e661d2c4bbbd | -0.67464 | -49.55171 | 2024-10-25 16:54:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| c0dbd16e-27ff-3a41-87b3-f28ac1892587 | -0.67177 | -49.55602 | 2024-10-25 16:54:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 245adb30-3945-3d9a-a341-7e7652bb73ef | -0.67118 | -49.55224 | 2024-10-25 16:54:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b713075e-6d86-38e5-99ec-b18599ec8c05 | -0.65153 | -49.53972 | 2024-10-25 16:54:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c3c9ecc7-0675-3373-b25f-eadb4f652324 | -0.63649 | -49.59627 | 2024-10-25 16:54:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1633b838-ab22-3dd9-87c1-21521a3717f9 | -0.29821 | -48.77642 | 2024-10-25 16:54:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 120dece6-2e63-3d53-83ea-6fdf9c30d2e0 | -0.29461 | -48.77697 | 2024-10-25 16:54:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fe099f05-561a-38d2-a844-ab3c4efca70b | -0.2282 | -48.79983 | 2024-10-25 16:54:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7875a7a2-1e55-3a07-b80f-7c0e30722add | -0.08146 | -49.61403 | 2024-10-25 16:54:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3ed717e9-1f91-3885-9939-7277df88e63a | -0.07799 | -49.61456 | 2024-10-25 16:54:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a01e4711-edfc-31b9-8d87-9364a7f3f11d | -0.07453 | -49.61509 | 2024-10-25 16:54:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 582f5782-73e8-350c-8375-fb5a4512c86c | -1.67009 | -48.74997 | 2024-10-25 16:54:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ea8cfeaf-df8d-36ad-8c40-778eb0e592da | -1.22366 | -48.81588 | 2024-10-25 16:54:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c0a2b14-bacc-3405-a9b2-80cc34539524 | -1.16782 | -48.82812 | 2024-10-25 16:54:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 58e27fb6-9f3a-3f20-8afe-ce9de2a6e75b | -0.79597 | -49.51826 | 2024-10-25 16:54:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1aa49291-9d54-3115-a5a0-d3186ca589ae | -1.80169 | -49.80517 | 2024-10-25 16:54:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9146faae-2b20-3b8a-a6dd-18f06f9b16c1 | -1.60549 | -49.94328 | 2024-10-25 16:54:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 3f7a4110-46c4-3831-86ae-3cf5707eeb38 | -1.58688 | -49.8904 | 2024-10-25 16:54:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6dd87d16-ebca-399e-8966-03ebc88451d8 | -1.3184 | -50.01743 | 2024-10-25 16:54:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3241a8c6-542d-3770-bedf-3e636289cfd7 | 2.63915 | -50.89288 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5b3948ac-b0fb-3bf2-9713-85b3b0cbc2eb | 2.63861 | -50.89651 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 889c9ab1-df15-3ef3-96e6-527d93060df2 | 2.55218 | -50.90968 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| accbc10f-5de9-3172-b302-17510c26de6b | 2.35384 | -50.89716 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b3f6a4cf-6475-3ab0-83c6-3fc1e3be1383 | 2.35101 | -50.89304 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bf1d6a6b-6b3c-34c7-af02-220b9080a29a | 2.35047 | -50.89665 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 99d938f4-b558-3b00-b938-ca33e5623524 | 2.33416 | -50.77562 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 345eaab0-c2f4-339f-8e81-1798c1f0a8e2 | 2.33077 | -50.77511 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 501fc9fd-93d2-3def-bbea-07e17d2a0e77 | 2.31645 | -50.76946 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ec00cf1-83ae-3fbb-a24d-bfe4b3e1635c | 2.31306 | -50.76895 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 09aae984-8259-3074-9b9c-56e7c3e94c1d | 2.31195 | -50.77621 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 709f8385-1355-3a57-8bc0-e8cf5b812dd1 | 2.31079 | -50.76117 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ab46305c-bd60-3c50-9da6-172e555ddfe8 | 2.31023 | -50.7648 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0332ff4b-6aac-34dd-aa51-df8ad351da3b | 2.30967 | -50.76844 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| be377300-8dac-3531-8bec-dfa2eaab03aa | 2.30912 | -50.77207 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 45728146-56cc-30c0-8e60-9b18440e3c36 | 2.29683 | -50.82957 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c776d16d-3874-3003-a9c7-63ba0104c101 | 0.8814 | -51.23499 | 2024-10-25 16:54:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 37.3 |
| a3ee0289-70fc-3727-b4a1-d33bdb4e0dbf | 0.82983 | -50.95029 | 2024-10-25 16:54:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d9d1f62-7e44-3524-9938-ee598759b5bd | 0.81781 | -50.20315 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9a80401c-aab4-3f33-a4ee-70c98efe9881 | 2.21989 | -50.766 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 833207ba-ff63-3065-90fe-bef428a39902 | 2.21532 | -50.74276 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b119686-6a90-3075-9bd7-6de1683a67d9 | 2.21127 | -50.84618 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 400d881f-1c73-3202-ae6c-e976974dd1e2 | 2.21072 | -50.8498 | 2024-10-25 16:54:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7f7a557e-b2fe-3ff2-be3b-137efcf9bb03 | 1.94017 | -50.8929 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 376971b4-5d75-3110-83d8-ebedf82fe81b | 1.93789 | -50.88521 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d316308e-ff91-37a4-bb73-d5e8c892756d | 1.93735 | -50.88879 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e52618fc-378a-319a-b11e-66147b6e3947 | 1.92004 | -50.91187 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5b46e0cb-cd55-3a6c-b81b-a9ff1ba356f4 | 1.87151 | -50.95943 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c26b7a1f-0f9d-3482-8338-9cc06d4bab3d | 1.82913 | -50.95247 | 2024-10-25 16:54:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9038ce2a-d3d9-35b9-9254-a0a83b66a1c7 | 1.82631 | -50.94839 | 2024-10-25 16:54:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4873f67a-4da9-32a1-95c1-f91664a45e30 | 1.82194 | -50.97693 | 2024-10-25 16:54:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a3c80a74-798a-3568-bb15-1ec9f033f4aa | 1.81837 | -50.47236 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 00f2c2e8-78e5-310c-bb52-12ff79cdb770 | 1.81553 | -50.46817 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| cb56ec8c-2a5a-3a47-95fa-e2411541400a | 1.81268 | -50.46397 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| a513c289-e663-304b-bcc2-4203e649ea19 | 1.80643 | -50.45925 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 19.3 |
| dedc2b7c-7df5-3341-b1e9-6be2cfa0b2f5 | 1.80301 | -50.45874 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9adc3aa2-2e57-3e7d-b111-73340c811e4e | 1.7996 | -50.45822 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a13808fc-66b9-36ac-b7b4-9b707adb2d20 | 1.79847 | -50.46559 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e28c6612-34b4-3f94-b404-0aa01c81a4dd | 1.79619 | -50.4577 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 1d938213-917e-3ae3-960f-db4158a77faf | 1.79562 | -50.46139 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f00a3efb-2fdf-3b15-a107-0862b6905385 | 1.7945 | -50.46875 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f8adab6-52ea-3a73-8d28-4f6e0c16ec9f | 1.79052 | -50.47192 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4562f467-027a-3649-bb5f-34031bd422bb | 1.78767 | -50.46772 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3c8dfbaa-0b29-3c11-9222-fbedebb8770f | 1.78426 | -50.4672 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 23a452a9-980e-3e25-9442-64fcdadfa7a4 | 1.7837 | -50.47088 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 80719c44-5335-3f8b-8cad-9f0b02d27229 | 1.78258 | -50.47824 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 13.9 |
| a687dc4b-3465-3935-ba63-c4435ed0b94f | 1.78201 | -50.48192 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 291fbf82-de2e-310e-b99a-56f3f653417f | 1.78145 | -50.4856 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e71393ac-a267-3a65-9eda-e1b56aaa64d9 | 1.78089 | -50.48927 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ab251d13-0a47-34e3-a1e2-0fd9e142d258 | 1.77977 | -50.49662 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9a98cae6-fd88-319b-8018-96d45948d5e4 | 1.77973 | -50.47404 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d77dafd-402c-399d-9a8a-e91f977c1882 | 1.7786 | -50.4814 | 2024-10-25 16:54:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7e878f22-1396-388d-8216-88ff7dae6988 | 0.72043 | -50.63853 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 51a826f9-66ff-3377-8eb6-7742d745efdb | 0.71989 | -50.64212 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7c920abf-2068-3390-a6aa-a4878a0054ca | 0.67295 | -50.75568 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 12e1c839-3380-3204-b6dc-159c9e0073f2 | 0.66959 | -50.75517 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b4c6cf4f-3194-3009-8a53-ff9874f3a011 | 0.66248 | -50.48638 | 2024-10-25 16:54:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4dcc74bb-9f38-3efb-a890-e2271c53614d | 0.66193 | -50.48999 | 2024-10-25 16:54:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0d4e58c4-2035-396f-8155-d39d3188d098 | 0.52374 | -50.77241 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| be2699da-5be8-3784-b55e-a0bbf2bf0739 | 0.52039 | -50.7719 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| eb836cb3-449e-32bc-bc52-2bf00e12dbbd | 0.35497 | -51.20927 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9b64617d-1178-3458-8a41-5b9ae0c8d0bd | 0.35444 | -51.21275 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5e073106-8752-3cd5-a86e-e3dbb95c082b | 0.31912 | -50.88889 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 1f7e979e-e093-30b2-9468-3e6b7e249f4f | 0.27396 | -50.87122 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e66ee3d-4bb0-34e2-b34e-3d4fd7237a73 | 0.26421 | -51.11338 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c18f19ec-6d73-3c39-89e2-cbe1a6fe42cb | 0.26368 | -51.11687 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| df71664a-e648-3020-9df8-e9edd26aa6dc | 0.26261 | -51.12383 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7753b630-8115-3d81-83b8-3ca7de9d66d2 | 0.25982 | -51.11984 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bf27d0c9-2f39-37d2-9cb9-a10633bd6a7b | 0.25928 | -51.12333 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c27075a1-8a59-3b0b-99c1-cb87b39fb3d2 | 0.25423 | -51.11187 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 02ab5cf1-e959-3888-a02a-4db19f56e07d | 0.24483 | -50.83794 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 04d17db7-98b1-39c1-8b35-fc1683f91c4c | 0.24229 | -50.83698 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d426728-58ef-3946-ab70-620322ff2574 | 0.22136 | -50.48077 | 2024-10-25 16:54:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e1040ce-97e2-3f81-8791-e95bbd76ded1 | 0.21799 | -50.48026 | 2024-10-25 16:54:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5f48265-e823-31c8-a16c-e8fd43299a85 | 0.21503 | -50.96946 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8052a78d-ed36-34eb-9c8c-5a1a9c822917 | 0.21214 | -50.94392 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 256ed07f-5c76-3db2-b3f6-e93c30f81347 | 0.14127 | -51.07267 | 2024-10-25 16:54:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README183.md)
