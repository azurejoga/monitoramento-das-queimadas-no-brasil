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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6e8669a-a203-3b1f-9e86-f0d60d592258 | -12.85734 | -48.09734 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eba3c821-552e-38a9-951c-3f40cd0f2fd9 | -12.7869 | -48.16577 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0288bd03-2637-3c69-835f-fdf74cb5eaca | -11.1222 | -45.11728 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8bb8c2d5-0998-36ad-bbe4-e2317ee93e2a | -6.04448 | -44.46933 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ba8d2b7-7c62-32c6-92bc-55c1f9a5753a | -13.54972 | -46.88664 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04862235-2cef-38e1-bcd1-b6047fa9623b | -13.97677 | -46.33338 | 2025-08-29 03:49:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0927175f-85ed-3d37-b249-0d6bfbfc4517 | -13.06947 | -46.35053 | 2025-08-29 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1417fec0-59b7-38eb-bad9-39e3359a038d | -6.32782 | -42.51013 | 2025-08-29 03:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 17afd9a4-1468-3055-96d6-d07d5702550f | -14.24771 | -48.06416 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e62038f-6ab3-39a5-ac74-5e49829c61f0 | -12.84591 | -48.09779 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7b73dcc7-e015-3ad0-8132-1b40101cc4f2 | -15.03684 | -48.12738 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fcff22c-fa96-3162-85be-d68903f06c97 | -13.55187 | -46.87551 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f0e935c-bc5e-3f33-8b82-d6688c1ad044 | -11.35089 | -43.54701 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 386e0b29-14a1-330b-b1eb-861269f8c114 | -5.91961 | -43.34672 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65bffad7-6c5c-3d95-8edd-bf7ba4c8f641 | -5.97712 | -43.36117 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 837627c8-35b3-39a9-9d9e-3b86593e52a2 | -15.83925 | -41.84871 | 2025-08-29 03:49:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bc7100e5-f1ce-3092-ad25-be5db577de4a | -5.47901 | -41.40974 | 2025-08-29 03:49:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ba66b8d2-d061-30b7-a784-d50c9e48d49f | -11.34272 | -43.569 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eee52d44-f89d-3b51-853c-45fd2d6e9755 | -15.78555 | -43.34679 | 2025-08-29 03:49:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abb2cab5-1449-33ee-8809-83875f39b8cc | -13.18273 | -45.28265 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 65669f26-4a8f-30b1-a653-8ba9317aca91 | -10.94961 | -46.88047 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74dc8ef3-b1d4-3b7b-aa6d-6c41d96e53a5 | -13.5128 | -46.94343 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11315236-53dd-3adc-ba09-149002d47c30 | -11.31844 | -43.56076 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 360cef42-af9a-3e06-b236-9305ebe0fbb0 | -13.40042 | -46.99034 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51c10cdf-3d73-3da3-918b-68fd08e50d5d | -12.0915 | -44.71962 | 2025-08-29 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 16ce5611-79e9-35ab-94c5-16ca5bb599d0 | -11.55562 | -46.3742 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29a19d2f-60dd-3ded-a878-72ab831a2d27 | -13.62278 | -48.20437 | 2025-08-29 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 726660cc-4c70-3612-b0bf-33bcff4c1e2e | -10.0324 | -48.0714 | 2025-08-29 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c89899e-2437-35af-87ca-b91e37b44bed | -13.39983 | -46.99339 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ad05551-66de-3b5c-ad42-fbf5ae90e8f5 | -13.19625 | -45.28529 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d6bfe661-f966-3d8a-bc5b-10c0fb2fe6ad | -13.40688 | -47.0109 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f061f50-453d-31c0-a8cf-ea761fdcc41c | -9.68498 | -48.32389 | 2025-08-29 03:49:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93c37b43-984f-3bff-a74d-ab3a03f0f72a | -6.16169 | -44.18992 | 2025-08-29 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5545534e-9964-3f18-b28d-4163989806d8 | -10.80462 | -46.35968 | 2025-08-29 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddcd6c11-7ecb-3bad-b8aa-b90df96448d0 | -11.22974 | -44.98977 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50c5441b-8857-39e0-a6c9-ff617831cc6c | -15.04865 | -48.12301 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0134499-c345-3043-ab77-3c0fffe5f50a | -11.24018 | -45.00806 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f0aa86d-2e14-37d8-9d0a-c9a19e7e7c26 | -5.61516 | -45.01437 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d3e899e-fde8-31b5-9317-6ccbc97cb30d | -11.32472 | -43.5737 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11c9ba93-a0c2-30df-8abb-d8c32414320b | -13.55804 | -46.92416 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ba43b92-4298-38f9-a29d-4e4d285df76a | -13.55914 | -46.86459 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4775cb6-11b3-3218-a6e0-a61114b95021 | -10.85519 | -47.49698 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 524bf807-1056-3bf4-a22e-ab2ca74d86fa | -13.07917 | -43.06438 | 2025-08-29 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 64e794a2-aa17-3fcb-8198-39c834343f25 | -11.08838 | -44.74992 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 65aa58e7-7cb2-3d01-b159-a9c60aba55ca | -11.29756 | -43.55006 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 598a0c8a-dac4-3fba-af98-7a8eb2961697 | -13.41105 | -46.96246 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fff6f374-fc6c-3d2f-b281-115cea882d6e | -6.27968 | -44.47549 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a04c131-f58a-3da6-853b-aa296179dd95 | -6.48895 | -43.53677 | 2025-08-29 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71ae2046-a7ad-3d3d-b972-a5e5a38f6d63 | -11.58628 | -46.37609 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1b6067d-15c2-33c5-8b52-0777b4fd80a3 | -6.5395 | -44.10221 | 2025-08-29 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ace1dee7-3eb1-32c7-86ae-f9b53ef5431d | -14.33212 | -48.65003 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66b5efdf-cffa-3876-b4a4-0c8786ffe141 | -10.9487 | -46.85667 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edc31d1d-b4ff-3849-aba4-1915b4bf70cb | -13.44897 | -46.95476 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d75ae3b5-50ea-3e56-9a27-52e4633bcd4d | -15.07081 | -48.12147 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 71758a5f-31db-3ab5-bc5a-7fef724c65c4 | -10.72364 | -47.01808 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a2ff470-7e82-3eaa-9210-765a12281d3c | -11.28924 | -43.54856 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fc45390-729e-384c-a4ce-930fc174e986 | -14.24039 | -48.06374 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0245a080-d4b9-347e-835f-389528f6a79e | -14.30792 | -51.90223 | 2025-08-29 03:49:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aed26b6d-d561-36f2-a225-351418f8d26b | -13.54493 | -46.93839 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c64d054b-b127-3842-9461-295dbbd39b0c | -11.08538 | -44.7469 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c9dffc5-40c9-3e54-a030-706ca10b5c80 | -12.09512 | -44.72483 | 2025-08-29 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 884d2e73-b259-3057-b663-e2517d0c404c | -11.5539 | -46.35606 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7dd7c281-c7fe-3397-9494-fd42a1bb64e6 | -11.23681 | -44.97672 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd885d3c-02a3-3578-851e-1f87f115e0f4 | -12.83507 | -48.15211 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08603bf1-0744-3a34-bae5-9449893bd996 | -10.84296 | -47.50198 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05d1c6df-cb11-36e7-8ee2-57ee9fe529c4 | -13.37598 | -46.87709 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1397fa25-c1a3-3e63-bd62-6f42f183962e | -15.12487 | -48.12149 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a3595eeb-d0f3-3a34-ac09-533fe794da0a | -5.86223 | -42.94212 | 2025-08-29 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 46dc9fba-eecc-3ad7-b111-a908fafb9a0c | -12.90636 | -48.13664 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad6d4d66-d4bd-3b1d-9e8f-e68f3462f9cd | -13.37482 | -46.88321 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1bbc7887-386c-3989-91ce-4d0c3543f7ed | -12.83687 | -48.11465 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cbd6b29-6888-3e18-8e1b-b0bd6bae3cc2 | -5.18144 | -46.072 | 2025-08-29 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8dabb4d0-8b48-362e-8ce6-2e0d3f6620fb | -11.56594 | -47.62135 | 2025-08-29 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 531bcca2-2a70-3104-8ae0-2ab83270c109 | -13.50487 | -46.8516 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a111a173-838a-3a46-a94c-224079123df4 | -12.8168 | -48.18803 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7161241a-941c-38c0-ba24-8dfc5cdc0822 | -11.26809 | -45.49168 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15f7c618-33c2-36bc-bc50-14d7ce44c037 | -3.42108 | -49.0429 | 2025-08-29 03:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5c260d55-d2d4-321f-9f8f-af9fc50037e7 | -12.90496 | -48.1438 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3d8b369b-d629-34dd-b200-a1ba00a900d2 | -12.81663 | -48.18732 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0ad03bc-b97c-3065-8d63-060671b74b50 | -6.54968 | -43.92807 | 2025-08-29 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6b091b7e-c80a-3a16-be8f-6d8953a8b9e9 | -12.07076 | -43.4698 | 2025-08-29 03:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02c526a1-ed3a-3466-b383-b9cb6fb6ce67 | -11.93686 | -46.70436 | 2025-08-29 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc9f3d59-8a82-3442-b8d2-da468428c6f1 | -11.6371 | -46.38049 | 2025-08-29 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f0e8616-9918-34eb-a869-6124d45960c5 | -11.28858 | -43.55238 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c13237f-33ae-3511-92f8-7dd4e3d8d361 | -5.78653 | -42.6113 | 2025-08-29 03:49:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 54bd913f-9fb1-382e-a53c-0b8f2cfc2812 | -6.44169 | -44.56573 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c113b45-4f88-3147-a9b6-6ef1b464534b | -4.11323 | -48.02098 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 399614ed-e0a1-3208-b494-a3712587b584 | -11.2317 | -45.0052 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f5026e1-c241-39bc-bdeb-77f9825114a4 | -12.78763 | -48.16206 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9756a1f6-7d5a-3df8-b01d-8d5357b3142e | -11.95563 | -44.84212 | 2025-08-29 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2a6e2bbd-270d-3831-96fc-2dd2f4b99ddc | -11.55473 | -46.35168 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 48496df8-db0e-3bcd-ad1d-11d0671d3f9d | -5.92257 | -43.3563 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de882e41-c745-3042-b273-d2aa7bae5e20 | -12.90566 | -48.14023 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b6d84cfe-bf30-3091-9f53-09d6b9123d38 | -12.70334 | -48.15592 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7057139d-69f7-37ad-acef-d6b8b67349c9 | -12.87273 | -48.13432 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e008417f-5280-3291-9790-45e5e4386823 | -12.84967 | -48.13595 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56ab7404-9770-3669-827c-4e52d738ec21 | -12.6802 | -48.18687 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 38da09f5-3d9c-3e2d-8072-bf8d108809c5 | -15.03612 | -48.13092 | 2025-08-29 03:49:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6214d7be-c225-333a-8cf1-f7c0b26ade59 | -5.61718 | -45.00241 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0fdab4fc-0b04-3baf-ad00-8613d6297935 | -11.57427 | -44.65227 | 2025-08-29 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README34.md)
