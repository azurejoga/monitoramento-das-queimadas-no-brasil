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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b53160a1-1e4a-3639-813a-bc2fcbdefe50 | -12.41213 | -52.15416 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4ef359d-267c-3d5c-a9df-e883749489e3 | -12.28645 | -52.47757 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4548d3f-7b02-3280-8079-8014aef54331 | -12.36433 | -49.97362 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9638f637-8a0f-3521-8662-0088e2a2c576 | -12.12999 | -54.66685 | 2025-05-21 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44758e93-5411-3e3f-8163-784f2a91cb38 | -12.03494 | -54.9725 | 2025-05-21 04:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6626e40b-e818-3231-82b2-4c6a122aa77f | -13.19646 | -47.26657 | 2025-05-21 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d63771b-80c2-3030-8146-5e2da3573be3 | -11.65192 | -48.10302 | 2025-05-21 04:42:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b9324fcf-0ebd-3e7c-ad31-4f04b78d09ef | -14.15554 | -45.46902 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d767398f-0a92-36aa-a1b9-41f09f29ae58 | -11.139 | -55.52903 | 2025-05-21 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0abeeaaf-a7d9-3be3-ac4e-edd1695fe0e9 | -11.15428 | -48.67643 | 2025-05-21 04:42:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39cca401-1539-35a2-b34c-8af49357feed | -12.34012 | -49.96266 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af5c08de-cfe9-328e-8818-eb50d78df23b | -12.36097 | -49.97308 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80e15a81-7241-32f6-9fe6-c498ead0d7bc | -12.50871 | -57.21955 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40a14e58-7d3a-361c-975f-25d664811d54 | -12.49156 | -57.18977 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f5e0597-1b98-385c-8c5d-0e3c43e3c100 | -11.41083 | -56.72887 | 2025-05-21 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13e54aa6-4097-3ef9-80e2-1d19f200b34b | -13.199 | -47.26937 | 2025-05-21 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60278884-7190-33f1-8bd7-d9bf26e0a93c | -14.02943 | -55.13741 | 2025-05-21 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bca5f96-8caa-3896-859b-77733cac9b91 | -10.8777 | -44.93804 | 2025-05-21 04:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bd5722b-e962-3c5b-b0aa-c4c90b46341a | -13.32848 | -45.40145 | 2025-05-21 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22dff5cf-2df0-3ea8-8a36-e2334d18f67e | -11.07343 | -54.77999 | 2025-05-21 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bda040a2-ef0b-3139-bdde-b30deafd3a14 | -12.69021 | -58.13464 | 2025-05-21 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ccdfb8b-031f-34e0-8899-2cbdb2f6c6b5 | -15.05 | -45.66402 | 2025-05-21 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 701d0b0f-08b0-30e8-94fc-1c4f54faafc1 | -12.2969 | -52.47533 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbe7c9f5-1b0a-355d-8190-5c25299c2419 | -10.79377 | -49.58745 | 2025-05-21 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1b905ad-90f1-3efe-a93b-384196b1d9f1 | -12.13076 | -54.66229 | 2025-05-21 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc5fb190-2e27-3c4c-aaf5-2e53f4647baa | -11.65007 | -58.26352 | 2025-05-21 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e820a38f-c568-3f1c-af56-3271910ea4f5 | -14.1677 | -45.47485 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 595f5bee-5938-3d70-b8c7-56c4f06e3cfc | -11.41008 | -56.73304 | 2025-05-21 04:42:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 125ca4ca-3c3a-329d-bcc2-6af4edbd41fa | -14.05714 | -53.37725 | 2025-05-21 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d966c30-1bdf-302e-bfca-0bf82475fa6a | -9.94393 | -49.74135 | 2025-05-21 04:42:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92e21148-a31e-3908-88e4-4ea68e571674 | -11.13696 | -53.93073 | 2025-05-21 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03f55214-5b4a-35c3-81bc-a1d0828cdb6f | -12.68558 | -58.1338 | 2025-05-21 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc009f8a-f7ca-36e5-a60e-a848611211a6 | -11.66731 | -54.94361 | 2025-05-21 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb2a163b-f737-386a-9ddb-4b1b3cdd9303 | -10.34156 | -51.69482 | 2025-05-21 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b17a2ed4-c1a9-339c-ae51-c22545851552 | -12.28825 | -52.48533 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 864f2cd6-153f-340e-91d3-7ed55f3fccdc | -11.29603 | -53.98148 | 2025-05-21 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| baff3431-fe5c-3c8d-9b56-8fe4572c91d0 | -10.82461 | -56.96133 | 2025-05-21 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9372bf14-7248-3ba3-8d5d-c0f60b186b7c | -12.28585 | -52.48128 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 138a6687-532a-380d-a7ed-457119d1cf02 | -13.80077 | -52.8946 | 2025-05-21 04:42:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dcbe042-f98f-3ad6-a371-79981bdfb289 | -10.6765 | -57.6016 | 2025-05-21 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91e2f7be-1758-301d-950b-80506f3f128b | -12.36713 | -49.97773 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae30928c-f7d6-3112-8820-a54f8947a2ca | -11.2088 | -49.16317 | 2025-05-21 04:42:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 367a4626-7119-3e2d-a6ec-40d3ce04d8eb | -11.07726 | -54.78065 | 2025-05-21 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8cfa075e-ff98-365e-8f71-7e8346e8005d | -15.51792 | -53.50958 | 2025-05-21 04:42:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 282a5fdc-a4d3-321e-a40e-9957d17687a4 | -11.07808 | -54.77591 | 2025-05-21 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f30eadcf-f38a-3e76-bc21-39223bade8e7 | -11.36283 | -55.12446 | 2025-05-21 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7643468d-d923-3dfc-963c-36fb49808f3d | -11.68965 | -47.80187 | 2025-05-21 04:42:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ae695bc-1947-39ca-bcfb-a9dd7bf4d815 | -11.88137 | -56.41835 | 2025-05-21 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0991df35-12cc-312d-ab01-f6b951616cc1 | -14.16239 | -45.48222 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17b4b032-b3c3-3049-b0aa-a11d0e5c1cdd | -12.34347 | -49.9632 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16bac64d-3f21-3b97-abad-76911abd2263 | -12.83801 | -47.39952 | 2025-05-21 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c020fdc-3048-3fcd-b8f2-0efb94e633dd | -12.84237 | -47.39561 | 2025-05-21 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a2efcb5-3cc3-3d97-b474-83df6cace3e4 | -12.07549 | -47.32544 | 2025-05-21 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd588c76-3ff0-31b2-8fc2-e70448b6fb2d | -12.64521 | -57.18645 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 991c8ce1-044c-3385-ad32-dc2599a3c35e | -12.07485 | -47.32982 | 2025-05-21 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 235354a5-1df8-344d-a565-f7273653091e | -14.04733 | -56.05987 | 2025-05-21 04:42:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2d727ab-979d-38e9-9197-2f30b7b13b04 | -12.35913 | -49.97307 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81021059-9467-3e66-aee5-84dd447c73c4 | -10.90569 | -48.54202 | 2025-05-21 04:42:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 393dabb3-e618-350e-8083-cace24787c76 | -11.14427 | -53.93199 | 2025-05-21 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6896eec2-a8b3-38bb-a8da-9fd94a5e7128 | -11.15538 | -48.68346 | 2025-05-21 04:42:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e38f161c-40bf-3620-9295-27aab0b5888c | -13.61746 | -55.45564 | 2025-05-21 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7ddf509e-1419-30bc-ac34-3223bd8620f6 | -11.1525 | -48.67915 | 2025-05-21 04:42:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d5de383-5267-345f-9baf-f0bb88f6fcaf | -11.35808 | -55.12876 | 2025-05-21 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ade2bb0-d991-368e-a971-9f94b2ab1dad | -14.68506 | -45.1087 | 2025-05-21 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f645dbf0-f831-379c-92f0-7b6a8d5a4a7b | -11.80771 | -44.27285 | 2025-05-21 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b0840e7-06f1-3939-a75f-e1cd8ea22447 | -11.80713 | -44.27725 | 2025-05-21 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f8de25f2-8e69-3d43-93ee-bdbfa0862168 | -12.33397 | -49.958 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 667f275a-fafd-3f1a-809c-8a1a23774bcf | -12.36488 | -49.97003 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2cff6cc-2422-321d-8534-1b8d71788e5b | -12.29227 | -52.48219 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| daa56a68-69b6-33b7-9ecb-18f88284f41a | -11.13769 | -53.92641 | 2025-05-21 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 272b8b9b-4a61-354c-84ef-aa30e3535049 | -10.24385 | -48.54007 | 2025-05-21 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1e856ff-b8a1-35f9-9780-eed35e5c8d78 | -13.3959 | -47.51394 | 2025-05-21 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcb87509-94fa-3321-b781-f942d4f233c2 | -14.0565 | -53.38112 | 2025-05-21 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fca8bda3-f8ea-3d1f-b1dc-58e3ccc297dc | -14.04793 | -56.06774 | 2025-05-21 04:42:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bdd017f-5501-3dde-9e1f-aae5384f6198 | -11.07261 | -54.78476 | 2025-05-21 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7e6c6383-3b06-3753-ae8a-40fef6c80c2c | -11.29311 | -53.97652 | 2025-05-21 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f6481923-a91b-3659-ae69-4dc1ea3913aa | -11.07644 | -54.78542 | 2025-05-21 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5e4d754b-4b0d-3c95-a7d7-1f137d2f26d1 | -11.78576 | -44.28102 | 2025-05-21 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9675189e-2477-3a8e-85b2-53a80cfff226 | -12.48208 | -57.19232 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61a5df93-6420-3cac-804f-7d070fa3dae6 | -12.6911 | -58.12981 | 2025-05-21 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28474897-b513-3a4d-8ec2-381cca520d2b | -10.59879 | -52.85048 | 2025-05-21 04:42:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44542aa8-15b8-3f61-a0f2-c4186ee6dc9a | -12.30372 | -52.47649 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94f10407-47f0-3d4e-8d5f-2e8494720998 | -12.64955 | -57.18731 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2125ccef-6be7-388f-9fd0-4abf500deeae | -12.29009 | -52.47419 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f5731f5-0b35-3280-95be-de5bfe05b507 | -12.56598 | -52.15664 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a59ae15e-fe22-3d1d-9d91-d8e47af7d055 | -11.46076 | -47.86551 | 2025-05-21 04:42:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36e62517-bb3a-32c6-9df1-7ad201fcba15 | -12.30249 | -52.48392 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 38c9939c-930e-3fae-be88-8b8b23f9273f | -12.29629 | -52.47905 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ce0239e-2c39-3746-85d6-eb8aadddcfc6 | -12.3031 | -52.4802 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c46fd0bf-a6f5-3947-8251-0ee0c739d2f8 | -11.14062 | -53.93136 | 2025-05-21 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3298413a-f4b1-3d78-a2b2-75a111eae7ee | -12.33621 | -49.96571 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72eb057e-cc94-344b-ae7a-6f2a7fe7a055 | -11.89405 | -49.19302 | 2025-05-21 04:42:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f87f7914-1a9e-3041-852b-cf747428b09e | -12.5544 | -52.24858 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32bb6cc4-aefe-3961-924f-5bf031757ec9 | -13.58154 | -47.36443 | 2025-05-21 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39c79eb7-3f0d-3b63-a3a1-d3741d149c1c | -12.13035 | -54.66434 | 2025-05-21 04:42:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cdb85fd-2c86-360c-8409-eac84a35a406 | -12.07853 | -47.3304 | 2025-05-21 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92949bcc-ef15-3104-bbaf-90d2bdb52d2e | -14.01899 | -55.13082 | 2025-05-21 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2d83f60-699e-3d97-af49-2b87df5184f5 | -11.35894 | -55.12379 | 2025-05-21 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 194b7ad2-2fa1-3b53-85df-e5267bf9f87b | -12.08157 | -47.33533 | 2025-05-21 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cae1772b-be00-3b4f-8480-47255e989cb8 | -11.64485 | -48.10194 | 2025-05-21 04:42:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README14.md)
