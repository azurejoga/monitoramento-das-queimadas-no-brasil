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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 645c7349-7610-3f75-8c0a-e53bcdbea2a3 | -11.79726 | -51.52496 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52f7a7a6-c7b6-38df-8a88-bb9d702d6df2 | -9.58685 | -46.68946 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc748809-48f3-31cd-a7fe-a478cbb168a6 | -12.90115 | -48.0516 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 93ff951a-b17e-3aff-8bd1-cc473f76da5f | -8.73128 | -47.00532 | 2025-09-04 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a614f99f-185d-3354-b721-45ca704ebb68 | -11.64518 | -52.20824 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5eb31fc9-0dfd-38bb-98f2-8ebd84bb9b97 | -12.47435 | -48.08302 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8798958a-6ee0-33ff-8d94-1d768f7d3764 | -11.85565 | -51.43988 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7271590c-e441-394f-ace7-2bdb28a58f2c | -14.13009 | -46.95827 | 2025-09-04 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8438f374-3f83-3011-9115-116c9d601154 | -11.59224 | -47.78776 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4579c38c-c366-3e4f-9311-1658d2885085 | -11.8856 | -51.53307 | 2025-09-04 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdf1fdab-bc08-37dd-ab75-5e67588a2b88 | -11.23722 | -44.96031 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 105be1fd-a30e-3c56-88f4-87a778474f38 | -10.31336 | -46.36459 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f08c3328-ced6-3301-b5c4-01798e899486 | -15.04984 | -50.04038 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ccb61dc-a8f2-3bce-9e9d-09617f57ccf8 | -12.7178 | -48.20237 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cbfde6a-975a-37b2-8270-43746561ba36 | -15.00954 | -50.04506 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 116cfce5-0615-33ab-bf16-b32f85ac9020 | -6.74197 | -58.72073 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8eba1467-4d0f-339b-be1a-faf75ea2c4a1 | -13.74285 | -46.93861 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70225202-d705-39b3-a031-402c4cb35600 | -14.57117 | -48.05001 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2a587106-3fd3-3dc0-99d9-b0d00acd6156 | -9.43704 | -46.77612 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bd90a33-d26c-3399-ab0a-53bf9381a979 | -11.59774 | -47.75274 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6de3cd99-40ac-37a6-80a2-c781341e8fb2 | -10.98765 | -46.8432 | 2025-09-04 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76033e2c-224e-37ac-84bf-dc20050c968f | -15.0046 | -50.03268 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 043ff638-d8db-3f20-9e7b-6f9d54edcfb4 | -10.49202 | -46.7716 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d24bd2fb-24e4-32c0-9033-224d4c780d0f | -12.46719 | -48.08545 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 692bdad1-8ec5-3275-bcc3-163cc29f980c | -14.80899 | -48.22739 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1129815f-b8a6-3382-9606-0fb64f67c277 | -6.74016 | -58.73514 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| e68e56b0-548e-3195-b3a9-ac7447923a83 | -8.37484 | -48.33325 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aaa30c1b-6252-3382-876b-716f28e1eeeb | -10.61279 | -55.40772 | 2025-09-04 04:27:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef3c0979-2508-3a7a-bbfe-57f0e6090bdb | -15.01136 | -50.03383 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8cf29717-26d7-3fcb-a42f-7ad7ce588d45 | -10.42959 | -50.38376 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1935ce17-9709-3a5b-b6a6-8ab7ed31895c | -14.3919 | -53.07104 | 2025-09-04 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60ecf80f-1a69-360d-8e32-9d8211d6922c | -14.21146 | -48.08912 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1df07c7d-45fe-35c3-adaf-19b9cdee476b | -12.60665 | -56.9991 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e0a0336-f389-3f54-900a-266a34c45b7e | -13.45338 | -46.83337 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c103cc98-c299-344e-b70c-a68025b5c252 | -11.85752 | -51.49567 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0246a642-967c-36b6-8b84-2ed823e4868e | -14.20926 | -48.08149 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d34d9cc6-5cd4-33f9-9634-b7df8deed31e | -10.61034 | -55.40565 | 2025-09-04 04:27:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23f8f2f2-b080-350a-9f10-35a2f8b0ae3b | -13.53573 | -47.02395 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a98256f-a7df-3327-95d9-f04d30b12b11 | -8.85946 | -52.01673 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1609be8-5b3a-35f2-b415-d020905f1aae | -14.59235 | -48.0249 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0496defe-633b-3e1a-9a25-81c9ed297807 | -12.50246 | -48.0551 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 498bc942-69bc-3757-8d76-48f108e9de83 | -9.44743 | -46.75626 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b5e0dfc-d38b-3095-a045-e80c4aac50fa | -11.6344 | -52.20112 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f70cb72c-ef14-372b-bc7c-1f4e6be3ad64 | -8.01458 | -45.79624 | 2025-09-04 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9576b98f-66e1-37bd-96ab-cf69090d1ff5 | -12.1818 | -53.88687 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 687e3d54-8496-303c-8ce1-9f19a5158d2e | -6.74557 | -58.74181 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8ff37828-5d09-3472-ae4b-a2d41f0bb317 | -8.03655 | -45.38358 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d7c9f73b-f3cc-3289-97b9-bfe1482d4e43 | -14.75969 | -48.08472 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27e4139f-ec0c-3c8a-9d6d-945a753647a3 | -15.13677 | -48.17546 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93773857-2703-37d1-ad66-583cac1f08a0 | -14.38873 | -53.06832 | 2025-09-04 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be487a1f-3b3d-3bff-8c14-cc8e76e3e505 | -11.7336 | -47.75359 | 2025-09-04 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7bf6373c-167c-3614-8ef1-b0316995b757 | -11.44336 | -46.90808 | 2025-09-04 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6e5562b-5d11-38cc-9215-4086bddd5527 | -11.78248 | -50.6769 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adb91e06-e3dd-3758-b109-3dc1d3983ce5 | -10.43097 | -50.3755 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 5aa4f809-b721-3cb1-b7d2-036770d511c4 | -11.64086 | -52.18698 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae884da3-3829-34f9-8635-b2dbcefdebbe | -11.59334 | -47.75921 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 958571f4-747a-3f55-b2c3-b29384a6ac50 | -9.06408 | -46.98733 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ae12706-5842-373c-a085-9817c7820343 | -11.2415 | -44.96368 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5eddfee1-e6f9-32e2-bbcc-09609609ec22 | -11.59609 | -47.76324 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15bf8e4a-d5e6-31fa-b7d1-51846b709160 | -7.60623 | -55.26916 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1a0680c-be72-328b-9727-5f16a040d83f | -15.03008 | -50.07589 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6654b977-0a9a-3506-84f5-79085a42c313 | -11.59609 | -47.78479 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a32d4f1e-7b11-3942-a248-7b647d9fc17f | -14.81561 | -48.20662 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4651aaf-6bf9-3be0-a9b6-067b6f65a945 | -12.89817 | -56.94878 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 88d56960-43b1-3b76-a320-16c530efb118 | -8.10127 | -46.26877 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e8c1d1b-3bfb-3470-aaaa-5174d1409c43 | -9.48 | -47.61074 | 2025-09-04 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d3fc6553-8082-3c5a-8b87-a4206ae33f55 | -12.49369 | -53.84426 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f15a3d7d-7bde-30c0-be47-231f2a7a0934 | -11.44282 | -46.9116 | 2025-09-04 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d23b349c-dfbb-348c-bde0-4710ca9beb9f | -10.74739 | -46.34868 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84a44fd1-e3ef-32a4-b7ea-ef4afdd88779 | -12.91146 | -56.94179 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 516b0e8c-1900-3e8d-9e1c-3cddb3673045 | -12.92536 | -48.06999 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77d18688-ac11-3cc5-9696-33c1c22339c0 | -8.07625 | -45.3491 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6382b648-1c82-394e-abac-265b247f11ab | -10.49415 | -53.65025 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40051f57-39fd-370c-bc63-0c4113f63a5e | -7.77973 | -50.95282 | 2025-09-04 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 376b5eb4-34b0-31d4-8a48-5d6ddcbeafba | -10.42891 | -50.27805 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 461fb619-53da-30e9-a334-663ebe7ed9bf | -15.04244 | -50.04313 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f3476aa-da11-3ff3-b5ef-4517bde98b30 | -7.2738 | -57.55967 | 2025-09-04 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15394b5d-e6c8-3cc8-916a-77dd2c4914f3 | -9.95946 | -51.64534 | 2025-09-04 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9c7c5b9-bb83-3762-a3d5-e39b4c26df59 | -10.03471 | -46.09857 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f54a845-2efb-3fbb-811d-b0b91a0115fa | -12.9902 | -48.07019 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b8ad3d7-21a1-30b7-9610-dea879d722af | -13.45368 | -46.93793 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8aca881a-7b69-394b-b5a3-9f039963957e | -12.47105 | -48.08248 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ae0673ae-4356-3b9f-853f-ea63fe8a8d5a | -13.30549 | -51.77299 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59a59cbf-e3d7-3093-bca2-a1271908cf13 | -14.82164 | -48.2331 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d944fe56-937b-3542-95a8-de0e93049797 | -9.50073 | -57.81791 | 2025-09-04 04:27:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97f54938-3220-3334-9399-205ccf4128ed | -10.15515 | -46.26714 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac3c4f0a-a449-3384-8a59-80e0db2b4b77 | -12.91161 | -56.93455 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e944042f-e26f-3260-a2b0-76caa0153f79 | -13.50397 | -47.01193 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0210d25a-63f1-3678-ae44-3b4b3335a783 | -10.98561 | -49.76506 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52cb5a69-69e2-3b1c-9b19-b2b78675f1a3 | -15.03276 | -48.1004 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35f29ca6-3354-39f4-a3a6-92e314cd8b48 | -8.35696 | -48.3156 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b177fa26-2974-3ab7-9d12-3c9137b42405 | -11.05886 | -45.40047 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1b34913-c29c-3490-b8be-38d15041b783 | -15.01867 | -50.08172 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7e501083-37a9-3a7c-8147-7fcde5e8b071 | -7.68935 | -50.26075 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bcb4690f-9bd5-32b9-8452-2f18a84505aa | -14.56953 | -48.0388 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| febe24ea-739e-3782-aee1-62dcb5ebdd99 | -15.01872 | -50.03126 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 699542ba-83fc-3511-a53e-396ae476baaf | -6.74654 | -58.73666 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| edd49e08-c973-3b09-b49a-1b0aeb6e4207 | -7.68539 | -48.73193 | 2025-09-04 04:27:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 1e03dac0-0358-3ab9-93d4-73a650b9e7c8 | -8.36045 | -48.29391 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f041ff0a-d20b-383f-9813-4b9141752b54 | -12.9745 | -54.77991 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README43.md)
